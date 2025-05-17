# populate_demo_data.py
from database import SessionLocal
from models import Product, Inventory, Sale
import datetime

# Initialize the database session
db = SessionLocal()

# === Sample Products ===
products = [
    {"name": "Apple iPhone 14", "category": "Electronics", "price": 999.99},
    {"name": "Samsung Galaxy S22", "category": "Electronics", "price": 899.99},
    {"name": "Sony WH-1000XM5", "category": "Audio", "price": 299.99},
    {"name": "Dell XPS 13", "category": "Computers", "price": 1199.99},
    {"name": "Asus ROG Strix", "category": "Computers", "price": 1499.99}
]

# Add products to DB
for product in products:
    db_product = Product(**product)
    db.add(db_product)
db.commit()

# === Sample Inventory ===
inventory_data = [
    {"product_id": 1, "quantity": 50},
    {"product_id": 2, "quantity": 40},
    {"product_id": 3, "quantity": 30},
    {"product_id": 4, "quantity": 20},
    {"product_id": 5, "quantity": 15}
]

for item in inventory_data:
    db_inventory = Inventory(**item)
    db.add(db_inventory)
db.commit()

# === Sample Sales Data ===
sales_data = [
    {"product_id": 1, "quantity": 5, "sale_date": datetime.datetime(2024, 12, 1)},
    {"product_id": 2, "quantity": 3, "sale_date": datetime.datetime(2024, 12, 2)},
    {"product_id": 3, "quantity": 2, "sale_date": datetime.datetime(2024, 12, 3)},
    {"product_id": 4, "quantity": 1, "sale_date": datetime.datetime(2024, 12, 4)},
    {"product_id": 5, "quantity": 4, "sale_date": datetime.datetime(2024, 12, 5)},
    {"product_id": 1, "quantity": 7, "sale_date": datetime.datetime(2024, 12, 6)},
    {"product_id": 2, "quantity": 6, "sale_date": datetime.datetime(2024, 12, 7)},
    {"product_id": 3, "quantity": 3, "sale_date": datetime.datetime(2024, 12, 8)}
]

for sale in sales_data:
    db_sale = Sale(**sale)
    db.add(db_sale)

db.commit()
db.close()

print("✅ Demo data populated successfully!")
