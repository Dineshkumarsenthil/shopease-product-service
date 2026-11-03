from typing import Optional

from fastapi import APIRouter, Query, status

from app.schemas.product_schema import ProductCreate, ProductResponse, ProductUpdate
from app.services import product_service

router = APIRouter(prefix="/api/products", tags=["Products"])


@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreate):
    return product_service.create_product(product)


@router.get("/", response_model=list[ProductResponse])
def list_products(
    category: Optional[str] = None,
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
):
    return product_service.get_all_products(category, skip, limit)


@router.get("/{product_id}", response_model=ProductResponse)
def get_product(product_id: int):
    return product_service.get_product(product_id)


@router.put("/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, product: ProductUpdate):
    return product_service.update_product(product_id, product)


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int):
    product_service.delete_product(product_id)