from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from app.core.database import get_db
from app.products import models, schemas

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.get("/", response_model=List[schemas.ProductOut])
def list_products(
    db: Session = Depends(get_db),
    category: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    sort_by: Optional[str] = Query("id", enum=["id", "price", "name"]),
    sort_order: Optional[str] = Query("asc", enum=["asc", "desc"]),
    page: int = 1,
    page_size: int = 10
):
    query = db.query(models.Product)

    # Filtering
    if category:
        query = query.filter(models.Product.category.ilike(f"%{category}%"))
    if min_price:
        query = query.filter(models.Product.price >= min_price)
    if max_price:
        query = query.filter(models.Product.price <= max_price)

    # Sorting
    sort_column = getattr(models.Product, sort_by)
    if sort_order == "desc":
        sort_column = sort_column.desc()
    query = query.order_by(sort_column)

    # Pagination
    offset = (page - 1) * page_size
    products = query.offset(offset).limit(page_size).all()

    return products


@router.get("/search", response_model=List[schemas.ProductOut])
def search_products(
    keyword: str = Query(..., min_length=1),
    db: Session = Depends(get_db)
):
    results = db.query(models.Product).filter(
        (models.Product.name.ilike(f"%{keyword}%")) |
        (models.Product.description.ilike(f"%{keyword}%"))
    ).all()
    return results


@router.get("/{product_id}", response_model=schemas.ProductOut)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
