from pydantic import BaseModel
from typing import Optional

class ProductBase(BaseModel):
    name: str
    price: float
    size: Optional[str] = None  # e.g. small, medium, large

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: str
