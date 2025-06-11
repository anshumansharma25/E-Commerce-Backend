from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.auth.dependencies import get_current_user
from app.cart.models import CartItem
from app.orders import models as order_models
from app.orders import schemas as order_schemas
from app.products.models import Product
from app.auth.models import User

router = APIRouter(
    prefix="",
    tags=["Orders"],
)


@router.post("/checkout", response_model=order_schemas.OrderResponse)
def checkout(
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    # 1. Get all cart items for the current user
    cart_items = db.query(CartItem).filter(CartItem.user_id == current_user.id).all()

    if not cart_items:
        raise HTTPException(status_code=400, detail="Cart is empty.")

    # 2. Calculate total price
    total_amount = sum(item.quantity * item.product.price for item in cart_items)

    # 3. Create new order
    order = order_models.Order(user_id=current_user.id, total=total_amount, status="Placed")
    db.add(order)
    db.commit()
    db.refresh(order)

    # 4. Add order items
    for item in cart_items:
        order_item = order_models.OrderItem(
            order_id=order.id,
            product_id=item.product_id,
            quantity=item.quantity,
            price=item.product.price
        )
        db.add(order_item)

    # 5. Clear cart
    db.query(CartItem).filter(CartItem.user_id == current_user.id).delete()

    db.commit()
    return order


@router.get("/orders", response_model=List[order_schemas.OrderSummary])
def get_order_history(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    orders = db.query(order_models.Order).filter(order_models.Order.user_id == current_user.id).all()
    return orders


@router.get("/orders/{order_id}", response_model=order_schemas.OrderDetail)
def get_order_detail(
    order_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    order = db.query(order_models.Order).filter_by(id=order_id, user_id=current_user.id).first()

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    # Build response manually to inject product_name from related Product
    return order_schemas.OrderDetail(
        id=order.id,
        user_id=order.user_id,
        created_at=order.created_at,
        total=order.total,
        status=order.status,
        items=[
            order_schemas.OrderItemResponse(
                product_id=item.product.id,
                product_name=item.product.name,
                quantity=item.quantity,
                price=item.product.price,  # or item.price if you store it at time of purchase
            )
            for item in order.items
        ]
    )


