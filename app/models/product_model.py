from dataclasses import dataclass
from datetime import datetime


@dataclass
class Product:
    id: int
    name: str
    description: str | None
    price: float
    stock: int
    category: str
    status: str
    created_at: datetime  