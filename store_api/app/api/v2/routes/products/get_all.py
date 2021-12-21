from typing import List
from fastapi import APIRouter
from app.models.v2.products import CompleteProductSchema
import app.api.v2.services.products.get_all as service

router = APIRouter()

@router.get('/products', response_model=List[CompleteProductSchema], status_code = 200)
async def get_all_products(
    category: int = None
):
    ''' List all existent products '''
    products = await service.get_all(category = category)

    return products
