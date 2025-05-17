import pytest
from httpx import AsyncClient
from main import app

@pytest.mark.asyncio
async def test_create_product():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/products", json={
            "name": "Test Product",
            "category": "Test Category",
            "price": 29.99
        })
    assert response.status_code == 201
    assert response.json()["message"] == "Product created successfully."

@pytest.mark.asyncio
async def test_get_products():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/products")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
