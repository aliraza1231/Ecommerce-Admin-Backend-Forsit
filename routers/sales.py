from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schemas
from database import get_db
from models import Sale, Product
from sqlalchemy import and_
from datetime import datetime

router = APIRouter()


@router.post("/", response_model=schemas.SaleCreate)
def record_sale(sale: schemas.SaleCreate, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == sale.product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found.")
    return crud.create_sale(db=db, sale=sale)


@router.get("/")
def get_sales(
    start_date: str = None,
    end_date: str = None,
    product_id: int = None,
    category: str = None,
    db: Session = Depends(get_db)
):
    """
    Retrieve sales data filtered by:
    - Date range (start_date, end_date)
    - Product ID
    - Category
    """
    # Convert date strings to datetime objects if they exist
    try:
        if start_date:
            start_date = datetime.strptime(start_date, "%Y-%m-%d")
        if end_date:
            end_date = datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD.")
    
    # Start query
    query = db.query(Sale).join(Product)

    # Apply filters
    if start_date and end_date:
        query = query.filter(and_(Sale.sale_date >= start_date, Sale.sale_date <= end_date))

    if product_id:
        query = query.filter(Sale.product_id == product_id)

    if category:
        query = query.filter(Product.category == category)

    
    sales = query.all()
    results = [
        {
            "sale_id": sale.id,
            "product_id": sale.product_id,
            "product_name": sale.product.name if sale.product else None,
            "category": sale.product.category if sale.product else None,
            "quantity": sale.quantity,
            "sale_date": sale.sale_date
        }
        for sale in sales
    ]

    return {"sales": results}
