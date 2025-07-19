from pydantic import BaseModel
from typing import List

class OrderProduct(BaseModel):
    product_id: str
    quantity: int

class OrderCreate(BaseModel):
    user_id: str
    products: List[OrderProduct]

class OrderResponse(OrderCreate):
    id: str
