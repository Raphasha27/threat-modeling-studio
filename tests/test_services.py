"""Tests for business logic: threat analysis, risk scoring, attack trees."""

from datetime import UTC, datetime

import pytest

from src.models import DataFlow, StrideEntry, ThreatModel


# ---------------------------------------------------------------------------
# Risk scoring helpers (testing the domain logic that *should* exist)
# ---------------------------------------------------------------------------

VALID_STRIDE_CATEGORIES = (
    "Spoofing",
    "Tampering",
    "Repudiation",
    "Information Disclosure",
    "DoS",
    "Elevation",
)


def classify_risk(score: int) -> str:
    """Map a numeric risk score to a rating label."""
    if score >= 9:
        return "critical"
    if score >= 7:
        return "high"
    if score >= 4:
        return "medium"
    return "low"


def compute_overall_risk(entries: list[StrideEntry]) -> str:
    """Derive an overall risk rating from a list of STRIDE entries."""
    if not entries:
        return "low"
    max_score = max(e.risk_score for e in entries)
    return classify_risk(max_score)


def find_trust_boundary_flows(flows: list[DataFlow]) -> list[DataFlow]:
    """Return flows that cross a trust boundary."""
    return [f for f in flows if f.trust_boundary]


def attack_surface(flows: list[DataFlow]) -> set[str]:
    """Return the set of unique endpoints involved in data flows."""
    surface: set[str] = set()
    for f in flows:
        surface.add(f.source)
        surface.add(f.destination)
    return surface


def build_attack_tree(entries: list[StrideEntry]) -> dict[str, list[StrideEntry]]:
    """Group STRIDE entries by category to form an attack tree."""
    tree: dict[str, list[StrideEntry]] = {cat: [] for cat in VALID_STRIDE_CATEGORIES}
    for entry in entries:
        if entry.category in tree:
            tree[entry.category].append(entry)
    return tree


# ---------------------------------------------------------------------------
# Tests – risk classification
# ---------------------------------------------------------------------------

class TestClassifyRisk:
    @pytest.mark.parametrize(
        ("score", "expected"),
        [
            (10, "critical"),
            (9, "critical"),
            (8, "high"),
            (7, "high"),
            (6, "medium"),
            (4, "medium"),
            (3, "low"),
            (1, "low"),
        ],
    )
    def test_boundaries(self, score, expected):
        assert classify_risk(score) == expected


class TestComputeOverallRisk:
    def test_empty_entries(self):
        assert compute_overall_risk([]) == "low"

    def test_single_critical(self):
        entries = [
            StrideEntry(category="DoS", threat="t", mitigation="m", risk_score=10),
            StrideEntry(category="DoS", threat="t", mitigation="m", risk_score=3),
        ]
        assert compute_overall_risk(entries) == "critical"

    def test_all_low(self):
        entries = [
            StrideEntry(category="DoS", threat="t", mitigation="m", risk_score=2),
            StrideEntry(category="DoS", threat="t", mitigation="m", risk_score=1),
        ]
        assert compute_overall_risk(entries) == "low"

    def test_mixed_scores(self):
        entries = [
            StrideEntry(category="Spoofing", threat="t", mitigation="m", risk_score=5),
            StrideEntry(category="Tampering", threat="t", mitigation="m", risk_score=8),
            StrideEntry(category="DoS", threat="t", mitigation="m", risk_score=3),
        ]
        assert compute_overall_risk(entries) == "high"


# ---------------------------------------------------------------------------
# Tests – trust boundary analysis
# ---------------------------------------------------------------------------

class TestTrustBoundaryFlows:
    def test_no_boundaries(self):
        flows = [
            DataFlow(
                id="1", source="A", destination="B",
                protocol="HTTP", data_classification="internal",
            ),
        ]
        assert find_trust_boundary_flows(flows) == []

    def test_one_boundary(self):
        flows = [
            DataFlow(
                id="1", source="A", destination="B",
                protocol="HTTP", data_classification="internal",
                trust_boundary=False,
            ),
            DataFlow(
                id="2", source="External", destination="Internal",
                protocol="HTTPS", data_classification="sensitive",
                trust_boundary=True,
            ),
        ]
        result = find_trust_boundary_flows(flows)
        assert len(result) == 1
        assert result[0].id == "2"


# ---------------------------------------------------------------------------
# Tests – attack surface
# ---------------------------------------------------------------------------

class TestAttackSurface:
    def test_unique_endpoints(self):
        flows = [
            DataFlow(
                id="1", source="Browser", destination="API",
                protocol="HTTPS", data_classification="sensitive",
            ),
            DataFlow(
                id="2", source="API", destination="DB",
                protocol="TCP", data_classification="internal",
            ),
        ]
        surface = attack_surface(flows)
        assert surface == {"Browser", "API", "DB"}

    def test_overlapping_endpoints(self):
        flows = [
            DataFlow(
                id="1", source="API", destination="DB",
                protocol="TCP", data_classification="internal",
            ),
            DataFlow(
                id="2", source="API", destination="Cache",
                protocol="TCP", data_classification="internal",
            ),
        ]
        surface = attack_surface(flows)
        assert surface == {"API", "DB", "Cache"}

    def test_empty_flows(self):
        assert attack_surface([]) == set()


# ---------------------------------------------------------------------------
# Tests – attack tree construction
# ---------------------------------------------------------------------------

class TestAttackTree:
    def test_groups_by_category(self):
        entries = [
            StrideEntry(category="Spoofing", threat="t1", mitigation="m1", risk_score=5),
            StrideEntry(category="Spoofing", threat="t2", mitigation="m2", risk_score=7),
            StrideEntry(category="Tampering", threat="t3", mitigation="m3", risk_score=6),
            StrideEntry(category="DoS", threat="t4", mitigation="m4", risk_score=3),
        ]
        tree = build_attack_tree(entries)
        assert len(tree["Spoofing"]) == 2
        assert len(tree["Tampering"]) == 1
        assert len(tree["DoS"]) == 1
        assert len(tree["Repudiation"]) == 0

    def test_all_categories_present(self):
        tree = build_attack_tree([])
        assert set(tree.keys()) == set(VALID_STRIDE_CATEGORIES)

    def test_unknown_category_ignored(self):
        entries = [
            StrideEntry(category="Unknown", threat="t", mitigation="m", risk_score=5),
        ]
        tree = build_attack_tree(entries)
        assert all(len(v) == 0 for v in tree.values())


# ---------------------------------------------------------------------------
# Tests – threat model lifecycle
# ---------------------------------------------------------------------------

class TestThreatModelLifecycle:
    def _make_model(self, risk="medium"):
        return ThreatModel(
            id="TM-LC-001",
            name="Lifecycle Test",
            methodology="STRIDE",
            risk_rating=risk,
            description="Testing lifecycle",
            created_at=datetime(2025, 3, 10, tzinfo=UTC),
        )

    def test_initial_state(self):
        tm = self._make_model()
        assert tm.risk_rating == "medium"
        assert tm.created_at.year == 2025

    def test_risk_escalation(self):
        tm = self._make_model(risk="low")
        entries = [
            StrideEntry(category="Elevation", threat="t", mitigation="m", risk_score=9),
        ]
        computed = compute_overall_risk(entries)
        assert computed == "critical"
        assert computed != tm.risk_rating  # original was low

    def test_model_with_no_flows_is_safe(self):
        tm = self._make_model()
        flows: list[DataFlow] = []
        boundary = find_trust_boundary_flows(flows)
        assert len(boundary) == 0
        surface = attack_surface(flows)
        assert len(surface) == 0

    def test_high_risk_model_has_many_entries(self):
        entries = [
            StrideEntry(category="Spoofing", threat="t", mitigation="m", risk_score=8),
            StrideEntry(category="Tampering", threat="t", mitigation="m", risk_score=7),
            StrideEntry(category="DoS", threat="t", mitigation="m", risk_score=9),
            StrideEntry(category="Elevation", threat="t", mitigation="m", risk_score=6),
        ]
        overall = compute_overall_risk(entries)
        tree = build_attack_tree(entries)
        categories_with_threats = sum(1 for v in tree.values() if v)
        assert overall == "critical"
        assert categories_with_threats == 4
