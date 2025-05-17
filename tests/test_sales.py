import pytest
from httpx import AsyncClient
from main import app

@pytest.mark.asyncio
async def test_get_sales():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/sales")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_get_sales_by_date_range():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/sales", params={
            "start_date": "2024-01-01",
            "end_date": "2024-12-31"
        })
    assert response.status_code == 200
    assert isinstance(response.json(), list)
