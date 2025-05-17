import pytest
from httpx import AsyncClient
from main import app

@pytest.mark.asyncio
async def test_analyze_revenue():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/analytics/revenue", params={
            "start_date": "2024-01-01",
            "end_date": "2024-12-31"
        })
    assert response.status_code == 200
    assert "total_revenue" in response.json()

@pytest.mark.asyncio
async def test_compare_revenue():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/analytics/compare-revenue", params={
            "start_date_1": "2024-01-01",
            "end_date_1": "2024-06-30",
            "start_date_2": "2024-07-01",
            "end_date_2": "2024-12-31"
        })
    assert response.status_code == 200
    assert "comparison" in response.json()
