from pydantic import BaseModel
from typing import Optional


class AddToCart(BaseModel):
    product_id: int
    quantity: int


class UpdateCartItem(BaseModel):
    quantity: int


class CartItemResponse(BaseModel):
    product_id: int
    product_name: str
    quantity: int
    subtotal: float

    class Config:
        orm_mode = True
