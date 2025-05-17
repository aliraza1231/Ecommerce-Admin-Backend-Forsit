from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import crud
from database import get_db
import schemas
from models import Inventory, Product, InventoryHistory

router = APIRouter()

@router.post("/", response_model=schemas.InventoryCreate)
def add_inventory(inventory: schemas.InventoryCreate, db: Session = Depends(get_db)):
    return crud.create_inventory(db=db, inventory=inventory)

LOW_STOCK_THRESHOLD = 10

@router.get("/low-stock")
def get_low_stock_items(db: Session = Depends(get_db)):
    low_stock = (
        db.query(Product.name, Inventory.quantity)
        .join(Product)
        .filter(Inventory.quantity < LOW_STOCK_THRESHOLD)
        .all()
    )
    return {"low_stock_items": low_stock}

@router.put("/{product_id}")
def update_inventory(product_id: int, quantity: int, db: Session = Depends(get_db)):
    inventory_item = db.query(Inventory).filter(Inventory.product_id == product_id).first()
    if inventory_item:
        inventory_item.quantity = quantity
        db.add(inventory_item)
        
        # Track the change in history
        history_entry = InventoryHistory(product_id=product_id, quantity=quantity)
        db.add(history_entry)
        
        db.commit()
        return {"message": "Inventory updated successfully"}
    else:
        return {"error": "Product not found"}
    

@router.get("/history/{product_id}")
def get_inventory_history(product_id: int, db: Session = Depends(get_db)):
    history = db.query(InventoryHistory).filter(InventoryHistory.product_id == product_id).all()
    return history