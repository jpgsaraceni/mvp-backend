from fastapi import APIRouter, HTTPException
from app.models.v2.products import ProductSchema
from app.models.v2.response import ResponseSchema
import app.api.v2.services.products.post as service
import app.api.v2.services.categories.get as categories_service

router = APIRouter()

@router.post('/products', response_model=ResponseSchema, status_code = 201)
async def create_product (payload: ProductSchema):
    ''' Create a new product '''
    category = await categories_service.get(payload.category_id)

    if not category:
        raise HTTPException(
            status_code = 404,
            detail = "Category not found"
        )

    new_product = await service.post(payload)

    response_object = {
        'message': "Product created successfully",
        'data': {
            'product_id': new_product
        }
    }

    return response_object
