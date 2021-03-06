from fastapi import APIRouter, HTTPException
from app.models.v1.products import ProductSchema
from app.models.v1.response import ResponseSchema
import app.api.v1.services.products.get as get_service
import app.api.v1.services.products.put as put_service

router = APIRouter()

@router.put('/products/{product_id}', response_model=ResponseSchema, status_code = 202)
async def update_product(product_id: int, payload: ProductSchema):
    ''' Update existent product by its ID '''
    if product_id < 1:
        raise HTTPException(status_code=400, detail="Product ID must be greater than 0")

    product = await get_service.get(product_id)

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    product = await put_service.put(product_id, payload)

    response_object = {
        'message': "Product updated successfully",
        'product_id': product
    }

    return response_object
    