from fastapi import APIRouter, HTTPException
from app.models.v2.products import ProductSchema
from app.models.v2.response import ResponseSchema
import app.api.v2.services.products.get as get_service
import app.api.v2.services.products.put as put_service
import app.api.v2.services.categories.get as categories_service

router = APIRouter()

@router.put('/products/{product_id}', response_model=ResponseSchema, status_code = 202)
async def update_product(product_id: int, payload: ProductSchema):
    ''' Update existent product by its ID '''
    if product_id < 1:
        raise HTTPException(
            status_code = 400,
            detail = "Product ID must be greater than 0"
        )

    product = await get_service.get(product_id)

    if not product:
        raise HTTPException(
            status_code = 404,
            detail = "Product not found"
        )

    category = await categories_service.get(payload.category_id)

    if not category:
        raise HTTPException(
            status_code = 404,
            detail = "Category not found"
        )

    product = await put_service.put(product_id, payload)

    response_object = {
        'message': "Product updated successfully",
        'data': {
            'product_id': product
        }
    }

    return response_object
    