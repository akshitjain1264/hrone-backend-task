from fastapi import APIRouter
from app.schemas.order import OrderCreate, OrderResponse
from app.models.order import order_helper
from app.database import db
from typing import List

router = APIRouter()

@router.post("/", status_code=201, response_model=OrderResponse)
async def create_order(order: OrderCreate):
    new_order = await db.orders.insert_one(order.dict())
    created = await db.orders.find_one({"_id": new_order.inserted_id})
    return order_helper(created)

@router.get("/{user_id}", response_model=List[OrderResponse])
async def get_orders(user_id: str, limit: int = 10, offset: int = 0):
    orders = await db.orders.find({"user_id": user_id}).skip(offset).limit(limit).to_list(length=limit)
    return [order_helper(o) for o in orders]
