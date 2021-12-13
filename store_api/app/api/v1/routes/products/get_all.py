from typing import List
from fastapi import APIRouter
from app.models.v1.products import ProductSchemaID
import app.api.v1.services.products.get_all as service

router = APIRouter()

@router.get('/products', response_model=List[ProductSchemaID], status_code = 200)
async def get_all_products():
    ''' List all existent products '''
    products = await service.get_all()

    return products
