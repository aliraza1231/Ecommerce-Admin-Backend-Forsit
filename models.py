from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Index
from sqlalchemy.orm import relationship
from database import Base
import datetime

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    category = Column(String(255))
    price = Column(Float)

class Inventory(Base):
    __tablename__ = "inventory"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)

class Sale(Base):
    __tablename__ = "sales"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)
    sale_date = Column(DateTime, default=datetime.datetime.utcnow)

class InventoryHistory(Base):
    __tablename__ = "inventory_history"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)
    change_date = Column(DateTime, default=datetime.datetime.utcnow)

Index('idx_product_id_inventory', Inventory.product_id)
Index('idx_product_id_sales', Sale.product_id)
Index('idx_product_id_history', InventoryHistory.product_id)
Index('idx_sale_date', Sale.sale_date)
Index('idx_category', Product.category)