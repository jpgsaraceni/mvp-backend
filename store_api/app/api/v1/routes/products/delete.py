from fastapi import APIRouter, HTTPException
from app.models.v1.response import ResponseSchema
import app.api.v1.crud.products.get as get_service
import app.api.v1.crud.products.delete as delete_service

router = APIRouter()

@router.delete('/products/{product_id}', response_model=ResponseSchema, status_code=200)
async def delete_product(product_id: int):
    ''' Delete existing product from the database '''
    if product_id < 1:
        raise HTTPException(status_code=404, detail="Product ID must be greater than 0")

    product = await get_service.get(product_id)

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    deleted_product = await delete_service.delete(product_id)

    response_object = {
        'message': "Product deleted successfully",
        'product_id': deleted_product
    }

    return response_object
