from typing import Optional
from pydantic import BaseModel, Field, ConfigDict


class ProductBase(BaseModel):
    name: str
    imageUrl: str = Field(validation_alias="image_url", serialization_alias="imageUrl")
    tag: str
    weight: str
    price: float
    rating: float
    oldPrice: Optional[float] = Field(default=None, validation_alias="old_price", serialization_alias="oldPrice")

    model_config = ConfigDict(populate_by_name=True, from_attributes=True)


class ProductCreate(ProductBase):
    pass


class ProductOut(ProductBase):
    id: int
