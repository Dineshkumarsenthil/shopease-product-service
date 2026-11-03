from datetime import datetime, timezone
from typing import Optional

from app.models.product_model import Product
from app.schemas.product_schema import ProductCreate, ProductUpdate


class ProductNotFoundError(Exception):
    pass


class InvalidProductIDError(Exception):
    pass


class DuplicateProductError(Exception):
    pass


_products: dict[int, Product] = {}
_next_id = 1


def _check_id(product_id: int) -> None:
    if product_id <= 0:
        raise InvalidProductIDError("Product ID must be a positive number")


def create_product(data: ProductCreate) -> Product:
    global _next_id
    if _next_id in _products:
        raise DuplicateProductError(f"Product with ID {_next_id} already exists")
    product = Product(
        id=_next_id,
        name=data.name,
        description=data.description,
        price=data.price,
        stock=data.stock,
        category=data.category,
        status=data.status.value,
        created_at=datetime.now(timezone.utc),
    )
    _products[_next_id] = product
    _next_id += 1
    return product


def get_all_products(category: Optional[str], skip: int, limit: int) -> list[Product]:
    items = list(_products.values())
    if category:
        items = [p for p in items if p.category.lower() == category.strip().lower()]
    return items[skip: skip + limit]


def get_product(product_id: int) -> Product:
    _check_id(product_id)
    product = _products.get(product_id)
    if product is None:
        raise ProductNotFoundError(f"Product with ID {product_id} was not found")
    return product


def update_product(product_id: int, data: ProductUpdate) -> Product:
    product = get_product(product_id)
    product.name = data.name
    product.description = data.description
    product.price = data.price
    product.stock = data.stock
    product.category = data.category
    product.status = data.status.value
    return product


def delete_product(product_id: int) -> None:
    get_product(product_id)
    del _products[product_id]