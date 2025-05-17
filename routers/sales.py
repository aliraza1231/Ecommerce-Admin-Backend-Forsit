from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import crud, schemas
from database import get_db
from models import Sale, Product
from sqlalchemy import and_

router = APIRouter()

@router.post("/", response_model=schemas.SaleCreate)
def record_sale(sale: schemas.SaleCreate, db: Session = Depends(get_db)):
    return crud.create_sale(db=db, sale=sale)

@router.get("/")
def get_sales(
    start_date: str = None,
    end_date: str = None,
    product_id: int = None,
    category: str = None,
    db: Session = Depends(get_db)
):
    query = db.query(Sale).join(Product)
    
    if start_date and end_date:
        query = query.filter(and_(Sale.sale_date >= start_date, Sale.sale_date <= end_date))
    
    if product_id:
        query = query.filter(Sale.product_id == product_id)
    
    if category:
        query = query.filter(Product.category == category)

    return query.all()