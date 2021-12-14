from fastapi import APIRouter, HTTPException
from models.v1.response import ResponseSchema
from api.v1.crud.products.get import get
from api.v1.crud.products.delete import delete

router = APIRouter()

@router.delete('/products/{product_id}', response_model=ResponseSchema, status_code=200)
async def delete_product(product_id: int):
    ''' Delete existing product from the database '''
    if product_id < 1:
        raise HTTPException(status_code=404, detail="Product ID must be greater than 0")

    product = await get(product_id)

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    deleted_product = await delete(product_id)

    response_object = {
        'message': "Product deleted successfully",
        'product_id': deleted_product
    }

    return response_object
