from typing import Optional
from pydantic import BaseModel, validator

class ProductSchema (BaseModel):
    ''' Schema for products '''
    name: str
    description: str
    price: float
    image: Optional[str]

    @validator('name')
    def name_must_be_greater_than3_and_smaller_than30(cls, value): #pylint: disable=no-self-argument
        ''' Validate product name lenght '''
        if not (len(value) > 2 and len(value) < 31):
            raise ValueError("Product name must be greater than 2 and smaller than 31 characters")

        return value.title()

    @validator('description')
    def description_must_be_greater_than3_and_smaller_than140(cls, value): #pylint: disable=no-self-argument
        ''' Validate product description lenght '''
        if not (len(value) > 2 and len(value) < 141):
            raise ValueError(
               "Product description must be greater than 2 and smaller than 141 characters")

        return value.title()

    @validator('price')
    def price_must_be_positive(cls, value): #pylint: disable=no-self-argument
        ''' Valiadte price value '''
        if value < 0:
            raise ValueError("Price must be positive")

        return float(value)

# inherit attributes from ProductSchema and add new ones
class ProductSchemaID (ProductSchema):
    ''' Schema for products with ID '''
    id: int
