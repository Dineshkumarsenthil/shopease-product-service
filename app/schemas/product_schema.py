from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator


class ProductStatus(str, Enum):
    ACTIVE = "Active"
    INACTIVE = "Inactive"


class ProductBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, examples=["Wireless Mouse"])
    description: Optional[str] = Field(None, max_length=500)
    price: float = Field(..., gt=0, examples=[799.0])
    stock: int = Field(..., ge=0, examples=[40])
    category: str = Field(..., min_length=1, max_length=50, examples=["Electronics"])
    status: ProductStatus = ProductStatus.ACTIVE

    @field_validator("name", "category")
    @classmethod
    def check_text(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("must not be empty")
        if not any(ch.isalpha() for ch in value):
            raise ValueError("must contain meaningful text, not only numbers or symbols")
        return value

    @field_validator("description")
    @classmethod
    def check_description(cls, value: Optional[str]) -> Optional[str]:
        if value is None:
            return None
        return value.strip() or None


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class ProductResponse(ProductBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)