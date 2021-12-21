from typing import Optional
from pydantic import BaseModel, validator

class ProductSchema (BaseModel):
    ''' Schema for products '''
    name: str
    description: str
    category_id: int
    price: float
    image: Optional[str]

    @validator('name')
    def name_must_be_greater_than3_and_smaller_than30(cls, name): #pylint: disable=no-self-argument
        ''' Validate product name lenght '''
        if not (len(name) > 2 and len(name) < 31):
            raise ValueError("Product name must be greater than 2 and smaller than 31 characters")

        return name.title()

    @validator('description')
    def description_must_be_greater_than3_and_smaller_than140(cls, description): #pylint: disable=no-self-argument
        ''' Validate product description lenght '''
        if not (len(description) > 2 and len(description) < 141):
            raise ValueError(
               "Product description must be greater than 2 and smaller than 141 characters")

        return description.capitalize()

    @validator('price')
    def price_must_be_positive(cls, price): #pylint: disable=no-self-argument
        ''' Valiadte price value '''
        if price < 0:
            raise ValueError("Price must be positive")

        return float(price)

    @validator('category_id')
    def category_must_be_greater_than_zero(cls, category): #pylint: disable=no-self-argument
        ''' Validate category greater than zero '''
        if category < 1:
            raise ValueError("Category must be greater than zero")

        return int(category)

# inherit attributes from ProductSchema and add new ones
class CompleteProductSchema (ProductSchema):
    ''' Schema for products with ID '''
    id: int
    category: str
