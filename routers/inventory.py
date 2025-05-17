from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud
from database import get_db
import schemas
from models import Inventory, Product, InventoryHistory

router = APIRouter()


@router.post("/", response_model=schemas.InventoryCreate)
def add_inventory(inventory: schemas.InventoryCreate, db: Session = Depends(get_db)):
    """
    Endpoint to add inventory for a product.
    """
    product = db.query(Product).filter(Product.id == inventory.product_id).first()
    
    if not product:
        raise HTTPException(
            status_code=404,
            detail=f"Product with ID {inventory.product_id} not found."
        )

    # Create inventory if product exists
    new_inventory = crud.create_inventory(db=db, inventory=inventory)
    return new_inventory


LOW_STOCK_THRESHOLD = 25

@router.get("/low-stock")
def get_low_stock_items(db: Session = Depends(get_db)):
    """
    Endpoint to fetch products that are low in stock.
    """
    try:
        low_stock = (
            db.query(Product.name, Inventory.quantity)
            .join(Inventory, Inventory.product_id == Product.id)
            .filter(Inventory.quantity < LOW_STOCK_THRESHOLD)
            .all()
        )
        
        if not low_stock:
            return {"message": "No products with low stock levels."}

        response = [{"product_name": item[0], "quantity": item[1]} for item in low_stock]
        return {"low_stock_items": response}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


@router.put("/{product_id}")
def update_inventory(product_id: int, quantity: int, db: Session = Depends(get_db)):
    """
    Endpoint to update inventory levels for a specific product.
    """
    inventory_item = db.query(Inventory).filter(Inventory.product_id == product_id).first()
    
    if not inventory_item:
        raise HTTPException(status_code=404, detail=f"Inventory for product ID {product_id} not found.")
    
    inventory_item.quantity = quantity
    db.add(inventory_item)


    history_entry = InventoryHistory(product_id=product_id, quantity=quantity)
    db.add(history_entry)
    
    db.commit()
    db.refresh(inventory_item)

    return {
        "message": f"Inventory for product ID {product_id} updated successfully.",
        "updated_quantity": quantity
    }


@router.get("/history/{product_id}")
def get_inventory_history(product_id: int, db: Session = Depends(get_db)):
    """
    Endpoint to fetch the inventory change history for a specific product.
    """
    history = db.query(InventoryHistory).filter(InventoryHistory.product_id == product_id).all()
    
    if not history:
        raise HTTPException(status_code=404, detail=f"No history found for product ID {product_id}")
    
    response = [
        {
            "product_id": item.product_id,
            "quantity": item.quantity,
            "change_date": item.change_date
        }
        for item in history
    ]
    
    return {"inventory_history": response}
