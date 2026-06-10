from pydantic import BaseModel, Field, ConfigDict
from src.core.enums import TypeProduct


class ProductBase(BaseModel):
    name: str = Field(..., min_length=5, max_length=10)
    category_product: TypeProduct


class ProductCreate(ProductBase):
    price: int
    pass


class ProductResponse(ProductBase):
    model_config = ConfigDict(from_attributes=True)
    id: int


class ProductPatch(BaseModel):
    name: int | None = None
    price: int | None = None
    category_product: TypeProduct | None = None
