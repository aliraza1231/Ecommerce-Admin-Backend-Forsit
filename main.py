from fastapi import FastAPI
from routers import products, inventory, sales, analytics
from database import engine, Base

# Create all tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI
app = FastAPI(
    title="E-commerce Admin API",
    description="API for managing products, inventory, and sales analytics",
    version="1.0.0",
)

# Register routers
app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(inventory.router, prefix="/inventory", tags=["Inventory"])
app.include_router(sales.router, prefix="/sales", tags=["Sales"])
app.include_router(analytics.router, prefix="/analytics", tags=["Analytics"])
