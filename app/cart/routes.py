from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.cart import models, schemas
from app.auth.dependencies import get_current_user
from app.core.database import get_db
from app.products.models import Product

router = APIRouter(prefix="/cart", tags=["Cart"])


@router.post("/", response_model=dict)
def add_to_cart(
        item: schemas.AddToCart,
        db: Session = Depends(get_db),
        user=Depends(get_current_user)
):
    product = db.query(Product).filter(Product.id == item.product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    cart_item = db.query(models.CartItem).filter_by(user_id=user.id, product_id=item.product_id).first()
    if cart_item:
        cart_item.quantity += item.quantity
    else:
        cart_item = models.CartItem(user_id=user.id, product_id=item.product_id, quantity=item.quantity)
        db.add(cart_item)
    db.commit()
    return {"message": "Item added to cart"}


@router.get("/", response_model=list[schemas.CartItemResponse])
def view_cart(
        db: Session = Depends(get_db),
        user=Depends(get_current_user)
):
    cart_items = db.query(models.CartItem).filter_by(user_id=user.id).all()
    response = []
    for item in cart_items:
        response.append(schemas.CartItemResponse(
            product_id=item.product_id,
            product_name=item.product.name,
            quantity=item.quantity,
            subtotal=item.quantity * item.product.price
        ))
    return response


@router.put("/{product_id}")
def update_cart_item(
        product_id: int,
        data: schemas.UpdateCartItem,
        db: Session = Depends(get_db),
        user=Depends(get_current_user)
):
    item = db.query(models.CartItem).filter_by(user_id=user.id, product_id=product_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found in cart")
    item.quantity = data.quantity
    db.commit()
    return {"message": "Cart item updated"}


@router.delete("/{product_id}")
def remove_from_cart(
        product_id: int,
        db: Session = Depends(get_db),
        user=Depends(get_current_user)
):
    item = db.query(models.CartItem).filter_by(user_id=user.id, product_id=product_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found in cart")
    db.delete(item)
    db.commit()
    return {"message": "Item removed from cart"}
