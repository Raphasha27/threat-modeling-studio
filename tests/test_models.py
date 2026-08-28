"""Tests for Pydantic data models/schemas."""

from datetime import UTC, datetime

import pytest
from pydantic import ValidationError

from src.models import DataFlow, StrideEntry, ThreatModel


class TestThreatModel:
    def test_create_valid(self):
        tm = ThreatModel(
            id="TM-001",
            name="Web App",
            methodology="STRIDE",
            risk_rating="high",
            description="A web app model",
            created_at=datetime.now(UTC),
        )
        assert tm.id == "TM-001"
        assert tm.methodology == "STRIDE"
        assert tm.risk_rating == "high"

    def test_all_methodologies_accepted(self):
        for meth in ("STRIDE", "PASTA", "VAST"):
            tm = ThreatModel(
                id="TM-001",
                name="Model",
                methodology=meth,
                risk_rating="low",
                description="desc",
                created_at=datetime(2025, 1, 1, tzinfo=UTC),
            )
            assert tm.methodology == meth

    def test_all_risk_ratings_accepted(self):
        for rating in ("critical", "high", "medium", "low"):
            tm = ThreatModel(
                id="TM-001",
                name="Model",
                methodology="STRIDE",
                risk_rating=rating,
                description="desc",
                created_at=datetime(2025, 1, 1, tzinfo=UTC),
            )
            assert tm.risk_rating == rating

    def test_missing_required_field_raises(self):
        with pytest.raises(ValidationError):
            ThreatModel(id="TM-001")  # type: ignore[call-arg]

    def test_wrong_type_raises(self):
        with pytest.raises(ValidationError):
            ThreatModel(
                id=123,  # type: ignore[arg-type]
                name="Model",
                methodology="STRIDE",
                risk_rating="low",
                description="desc",
                created_at="not-a-date",  # type: ignore[arg-type]
            )

    def test_model_serialization_roundtrip(self):
        now = datetime(2025, 6, 15, 12, 0, 0, tzinfo=UTC)
        tm = ThreatModel(
            id="TM-002",
            name="API Model",
            methodology="PASTA",
            risk_rating="critical",
            description="Critical API",
            created_at=now,
        )
        data = tm.model_dump()
        restored = ThreatModel(**data)
        assert restored == tm
        assert isinstance(data["created_at"], datetime)
        assert data["created_at"].year == 2025


class TestStrideEntry:
    def test_create_valid(self):
        entry = StrideEntry(
            category="Spoofing",
            threat="Stolen session token",
            mitigation="Implement MFA",
            risk_score=8,
        )
        assert entry.category == "Spoofing"
        assert entry.risk_score == 8

    def test_all_stride_categories(self):
        categories = (
            "Spoofing",
            "Tampering",
            "Repudiation",
            "Information Disclosure",
            "DoS",
            "Elevation",
        )
        for cat in categories:
            entry = StrideEntry(
                category=cat,
                threat="threat",
                mitigation="fix",
                risk_score=5,
            )
            assert entry.category == cat

    def test_risk_score_lower_bound(self):
        entry = StrideEntry(
            category="DoS",
            threat="t",
            mitigation="m",
            risk_score=1,
        )
        assert entry.risk_score == 1

    def test_risk_score_upper_bound(self):
        entry = StrideEntry(
            category="DoS",
            threat="t",
            mitigation="m",
            risk_score=10,
        )
        assert entry.risk_score == 10

    def test_missing_category_raises(self):
        with pytest.raises(ValidationError):
            StrideEntry(threat="t", mitigation="m", risk_score=5)  # type: ignore[call-arg]

    def test_missing_threat_raises(self):
        with pytest.raises(ValidationError):
            StrideEntry(category="DoS", mitigation="m", risk_score=5)  # type: ignore[call-arg]

    def test_missing_mitigation_raises(self):
        with pytest.raises(ValidationError):
            StrideEntry(category="DoS", threat="t", risk_score=5)  # type: ignore[call-arg]

    def test_missing_risk_score_raises(self):
        with pytest.raises(ValidationError):
            StrideEntry(category="DoS", threat="t", mitigation="m")  # type: ignore[call-arg]

    def test_serialization_roundtrip(self):
        entry = StrideEntry(
            category="Tampering",
            threat="API modification",
            mitigation="HTTPS",
            risk_score=7,
        )
        data = entry.model_dump()
        restored = StrideEntry(**data)
        assert restored == entry

    def test_json_serialization(self):
        entry = StrideEntry(
            category="Elevation",
            threat="Privilege escalation",
            mitigation="RBAC",
            risk_score=9,
        )
        json_str = entry.model_dump_json()
        restored = StrideEntry.model_validate_json(json_str)
        assert restored.category == "Elevation"


class TestDataFlow:
    def test_create_valid_with_trust_boundary(self):
        df = DataFlow(
            id="DF-01",
            source="Browser",
            destination="API Gateway",
            protocol="HTTPS",
            data_classification="sensitive",
            trust_boundary=True,
        )
        assert df.trust_boundary is True

    def test_trust_boundary_defaults_false(self):
        df = DataFlow(
            id="DF-02",
            source="A",
            destination="B",
            protocol="HTTP",
            data_classification="public",
        )
        assert df.trust_boundary is False

    def test_missing_required_fields_raises(self):
        with pytest.raises(ValidationError):
            DataFlow(id="DF-03")  # type: ignore[call-arg]

    def test_source_and_destination_distinct(self):
        df = DataFlow(
            id="DF-04",
            source="Server",
            destination="Database",
            protocol="TCP",
            data_classification="internal",
        )
        assert df.source != df.destination

    def test_all_protocols_accepted(self):
        for proto in ("HTTPS", "HTTP", "TCP", "UDP", "gRPC", "WebSocket"):
            df = DataFlow(
                id="DF-05",
                source="A",
                destination="B",
                protocol=proto,
                data_classification="public",
            )
            assert df.protocol == proto

    def test_serialization_roundtrip(self):
        df = DataFlow(
            id="DF-06",
            source="Client",
            destination="Server",
            protocol="HTTPS",
            data_classification="confidential",
            trust_boundary=True,
        )
        data = df.model_dump()
        restored = DataFlow(**data)
        assert restored == df

    def test_trust_boundary_crossing(self):
        df_in = DataFlow(
            id="IN",
            source="Internal",
            destination="Internal",
            protocol="HTTP",
            data_classification="internal",
            trust_boundary=False,
        )
        df_cross = DataFlow(
            id="CROSS",
            source="External",
            destination="Internal",
            protocol="HTTPS",
            data_classification="sensitive",
            trust_boundary=True,
        )
        assert df_in.trust_boundary is False
        assert df_cross.trust_boundary is True


class TestModelInteractions:
    """Tests that verify models work together correctly."""

    def test_threat_model_with_stride_entries(self):
        tm = ThreatModel(
            id="TM-100",
            name="Combined Test",
            methodology="STRIDE",
            risk_rating="high",
            description="Integration test",
            created_at=datetime.now(UTC),
        )
        entries = [
            StrideEntry(
                category="Spoofing",
                threat="Impersonation",
                mitigation="MFA",
                risk_score=8,
            ),
            StrideEntry(
                category="Tampering",
                threat="Data modification",
                mitigation="Integrity checks",
                risk_score=7,
            ),
        ]
        high_risk = [e for e in entries if e.risk_score >= 7]
        assert len(high_risk) == 2
        assert tm.methodology == "STRIDE"

    def test_data_flow_risk_assessment(self):
        flows = [
            DataFlow(
                id="DF-A",
                source="Browser",
                destination="API",
                protocol="HTTPS",
                data_classification="sensitive",
                trust_boundary=True,
            ),
            DataFlow(
                id="DF-B",
                source="API",
                destination="DB",
                protocol="TCP",
                data_classification="internal",
                trust_boundary=False,
            ),
        ]
        boundary_crossings = [f for f in flows if f.trust_boundary]
        assert len(boundary_crossings) == 1
        assert boundary_crossings[0].id == "DF-A"
