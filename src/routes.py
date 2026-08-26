"""Threat modeling routes."""

from datetime import UTC, datetime

from fastapi import APIRouter

from src.models import DataFlow, StrideEntry, ThreatModel

router = APIRouter(prefix="/api/v1", tags=["threats"])


@router.get("/models")
async def list_models():
    return [
        ThreatModel(
            id="TM-001",
            name="Web Application Threat Model",
            methodology="STRIDE",
            risk_rating="high",
            description="Threat model for customer-facing web application",
            created_at=datetime.now(UTC),
        ),
    ]


@router.get("/models/{model_id}/stride")
async def get_stride(model_id: str):
    return [
        StrideEntry(
            category="Spoofing",
            threat="Attacker impersonates legitimate user via stolen session token",
            mitigation="Implement MFA and short-lived JWT tokens",
            risk_score=8,
        ),
        StrideEntry(
            category="Tampering",
            threat="API request modification in transit",
            mitigation="Enforce HTTPS with certificate pinning",
            risk_score=7,
        ),
        StrideEntry(
            category="Information Disclosure",
            threat="Database error messages expose schema details",
            mitigation="Implement generic error responses and input validation",
            risk_score=6,
        ),
    ]


@router.get("/models/{model_id}/flows")
async def get_data_flows(model_id: str):
    return [
        DataFlow(
            id="DF-01",
            source="Browser",
            destination="API Gateway",
            protocol="HTTPS",
            data_classification="sensitive",
            trust_boundary=True,
        ),
        DataFlow(
            id="DF-02",
            source="API Gateway",
            destination="Application Server",
            protocol="HTTP",
            data_classification="sensitive",
            trust_boundary=False,
        ),
    ]
