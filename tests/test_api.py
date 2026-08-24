"""Additional tests for Threat Modeling Studio."""

import pytest
from httpx import ASGITransport, AsyncClient
from src.main import app


@pytest.mark.asyncio
async def test_list_models():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        resp = await client.get("/api/v1/models")
        assert resp.status_code == 200
        assert resp.json()[0]["methodology"] == "STRIDE"


@pytest.mark.asyncio
async def test_stride():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        resp = await client.get("/api/v1/models/TM-001/stride")
        assert resp.status_code == 200
        assert resp.json()[0]["category"] == "Spoofing"
