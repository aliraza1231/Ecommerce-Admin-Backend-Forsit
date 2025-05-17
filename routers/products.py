from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud
from database import get_db
import schemas
from models import Product

router = APIRouter()


@router.post("/", response_model=schemas.ProductCreate)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    """
    Endpoint to create a new product.
    """
    # Check if a product with the same name and category already exists
    existing_product = db.query(Product).filter(
        Product.name == product.name, Product.category == product.category
    ).first()
    
    if existing_product:
        raise HTTPException(
            status_code=400,
            detail=f"Product '{product.name}' in category '{product.category}' already exists."
        )

    new_product = crud.create_product(db=db, product=product)
    return new_product


@router.get("/", response_model=list[schemas.ProductCreate])
def get_all_products(db: Session = Depends(get_db)):
    """
    Endpoint to fetch all products.
    """
    products = db.query(Product).all()
    return products


@router.get("/{product_id}", response_model=schemas.ProductCreate)
def get_product(product_id: int, db: Session = Depends(get_db)):
    """
    Endpoint to fetch a product by its ID.
    """
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(
            status_code=404, detail=f"Product with ID {product_id} not found."
        )
    return product


@router.put("/{product_id}", response_model=schemas.ProductCreate)
def update_product(product_id: int, updated_product: schemas.ProductCreate, db: Session = Depends(get_db)):
    """
    Endpoint to update product details.
    """
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(
            status_code=404, detail=f"Product with ID {product_id} not found."
        )
    
    product.name = updated_product.name
    product.category = updated_product.category
    product.price = updated_product.price
    db.commit()
    db.refresh(product)
    return product

@router.delete("/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    """
    Endpoint to delete a product by its ID.
    """
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(
            status_code=404, detail=f"Product with ID {product_id} not found."
        )
    
    db.delete(product)
    db.commit()
    return {"message": f"Product with ID {product_id} has been deleted successfully."}
