from fastapi import APIRouter, HTTPException
from app.models.v2.products import CompleteProductSchema
import app.api.v2.services.products.get as service


router = APIRouter()

@router.get('/products/{product_id}', response_model=CompleteProductSchema, status_code = 200)
async def get_product_by_id(product_id: int):
    ''' Get an especific existent product by its ID'''
    if product_id < 1:
        raise HTTPException(
            status_code = 400,
            detail = "Product ID must be greater than 0"
        )

    product = await service.get(product_id)

    if not product:
        raise HTTPException(
            status_code = 404,
            detail = "Product not found"
        )

    return product
