from fastapi import APIRouter, Query
from app.schemas.product import ProductCreate, ProductResponse
from app.models.product import product_helper
from app.database import db
from typing import List

router = APIRouter()

@router.post("/", status_code=201, response_model=ProductResponse)
async def create_product(product: ProductCreate):
    new_product = await db.products.insert_one(product.dict())
    created = await db.products.find_one({"_id": new_product.inserted_id})
    return product_helper(created)

@router.get("/", response_model=List[ProductResponse])
async def list_products(
    name: str = None,
    size: str = None,
    limit: int = 10,
    offset: int = 0
):
    query = {}
    if name:
        query["name"] = {"$regex": name, "$options": "i"}
    if size:
        query["size"] = size
    products = await db.products.find(query).skip(offset).limit(limit).to_list(length=limit)
    return [product_helper(p) for p in products]
