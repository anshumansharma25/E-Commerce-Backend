from pydantic import BaseModel
from typing import List
from datetime import datetime


# ----- Order Item Schema -----
class OrderItemResponse(BaseModel):
    product_id: int
    product_name: str
    quantity: int
    price: float  # Price per unit at time of purchase

    class Config:
        orm_mode = True


# ----- Order Summary Schema -----
# Used for listing past orders (/orders)
class OrderSummary(BaseModel):
    id: int
    created_at: datetime
    total: float
    status: str

    class Config:
        orm_mode = True


# ----- Order Detail Schema -----
# Used for viewing full order details (/orders/{id})
class OrderDetail(BaseModel):
    id: int
    user_id: int
    created_at: datetime
    total: float
    status: str
    items: List[OrderItemResponse]

    class Config:
        orm_mode = True


# ----- Order Response Schema (after Checkout) -----
# Used for /checkout return value
class OrderResponse(OrderDetail):
    pass
