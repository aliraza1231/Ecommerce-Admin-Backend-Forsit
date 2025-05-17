from pydantic import BaseModel
from typing import Optional
import datetime

class ProductCreate(BaseModel):
    name: str
    category: str
    price: float

class InventoryCreate(BaseModel):
    product_id: int
    quantity: int

class SaleCreate(BaseModel):
    product_id: int
    quantity: int
    sale_date: Optional[datetime.datetime] = None
