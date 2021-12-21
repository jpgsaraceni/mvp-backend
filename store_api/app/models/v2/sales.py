from typing import Optional
from datetime import datetime
from pydantic import BaseModel, validator

class SalesSchema(BaseModel):
    ''' Sales schema '''
    client_id: int
    product_id: int
    payment_method_id: int
    amount: int
    price: float
    valid_for: Optional[int]

    @validator('client_id')
    def client_it_is_greater_than_zero (cls, client_id): # pylint: disable=no-self-argument
        ''' Validate client_id greater than zero '''
        if client_id < 1:
            raise ValueError('The client_id must be greater than zero')
        else:
            return client_id

    @validator('product_id')
    def product_it_is_greater_than_zero (cls, product_id): # pylint: disable=no-self-argument
        ''' Validate product_id greater than zero'''
        if product_id < 1:
            raise ValueError('The product_id must be greater than zero')
        else:
            return product_id

    @validator('payment_method_id')
    def payment_method_it_is_greater_than_zero(cls, payment_method_id): # pylint: disable=no-self-argument
        ''' Validate product_id greater than zero '''
        if payment_method_id < 1:
            raise ValueError('The payment_method_id must be greater than zero')
        else:
            return payment_method_id

    @validator('amount')
    def amount_is_greater_than_zero (cls, amount): # pylint: disable=no-self-argument
        ''' Validate amount greater than zero '''
        if amount < 1:
            raise ValueError('The amount must be greater than zero')
        else:
            return amount

    @validator('price')
    def price_is_greater_than_zero (cls, price): # pylint: disable=no-self-argument
        ''' Validate price positive  '''
        if price < 0:
            raise ValueError('The price must be positive')
        else:
            return float(price)

class SalesSchemaConsult (SalesSchema):
    ''' Sales schema for consult '''
    id: int
    valid_until: Optional[datetime]
    created_at: datetime
