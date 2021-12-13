from fastapi import APIRouter
from app.models.v1.products import ProductSchema
from app.models.v1.response import ResponseSchema
import app.api.v1.crud.products.post as service

router = APIRouter()

@router.post('/products', response_model=ResponseSchema, status_code = 201)
async def create_product (payload: ProductSchema):
    ''' Create a new product '''
    new_product = await service.post(payload)

    response_object = {
        'message': "Product created successfully",
        'product_id': new_product
    }

    return response_object
