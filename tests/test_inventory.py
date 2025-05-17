import pytest
from httpx import AsyncClient
from main import app

@pytest.mark.asyncio
async def test_get_inventory():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/inventory")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_update_inventory():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.put("/inventory/1", json={"quantity": 50})
    assert response.status_code == 200
    assert response.json()["message"] == "Inventory updated successfully."

@pytest.mark.asyncio
async def test_low_stock_alert():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/inventory/low-stock")
    assert response.status_code == 200
    assert isinstance(response.json()["low_stock_items"], list)
