from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Sale, Product
from sqlalchemy import func

router = APIRouter()

@router.get("/revenue")
def get_revenue(period: str, db: Session = Depends(get_db)):
    if period == "daily":
        revenue = db.query(func.sum(Sale.quantity * Product.price)).filter(
            func.date(Sale.sale_date) == func.current_date()
        ).scalar()
    elif period == "monthly":
        revenue = db.query(func.sum(Sale.quantity * Product.price)).filter(
            func.month(Sale.sale_date) == func.month(func.current_date())
        ).scalar()
    elif period == "yearly":
        revenue = db.query(func.sum(Sale.quantity * Product.price)).filter(
            func.year(Sale.sale_date) == func.year(func.current_date())
        ).scalar()
    else:
        return {"error": "Invalid period specified"}
    
    return {"period": period, "revenue": revenue}

def calculate_revenue(db, start_date, end_date, category=None):
    query = db.query(func.sum(Sale.quantity * Product.price)).join(Product)
    
    if category:
        query = query.filter(Product.category == category)
    
    query = query.filter(Sale.sale_date >= start_date, Sale.sale_date <= end_date)
    revenue = query.scalar()
    return revenue if revenue else 0

@router.get("/compare-revenue")
def compare_revenue(
    start_date_1: str,
    end_date_1: str,
    start_date_2: str,
    end_date_2: str,
    category: str = None,
    db: Session = Depends(get_db)
):
    """
    Compare revenue between two date ranges or categories.
    """
    rev_1 = calculate_revenue(db, start_date_1, end_date_1, category)
    rev_2 = calculate_revenue(db, start_date_2, end_date_2, category)

    return {
        "comparison": {
            "Period 1": {"Start": start_date_1, "End": end_date_1, "Revenue": rev_1},
            "Period 2": {"Start": start_date_2, "End": end_date_2, "Revenue": rev_2},
            "Difference": rev_2 - rev_1
        }
    }