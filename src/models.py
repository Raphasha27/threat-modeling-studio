"""Pydantic models for Threat Modeling Studio."""

from datetime import datetime

from pydantic import BaseModel


class ThreatModel(BaseModel):
    id: str
    name: str
    methodology: str  # STRIDE, PASTA, VAST
    risk_rating: str  # critical, high, medium, low
    description: str
    created_at: datetime


class StrideEntry(BaseModel):
    category: str  # Spoofing, Tampering, Repudiation, InfoDisclosure, DoS, Elevation
    threat: str
    mitigation: str
    risk_score: int  # 1-10


class DataFlow(BaseModel):
    id: str
    source: str
    destination: str
    protocol: str
    data_classification: str
    trust_boundary: bool = False
