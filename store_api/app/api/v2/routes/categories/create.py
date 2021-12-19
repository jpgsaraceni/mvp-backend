from fastapi import APIRouter
from app.models.v2.categories import CategoriesSchema
from app.models.v2.response import ResponseSchema
import app.api.v2.services.categories.post as service

router = APIRouter()

@router.post('/categories', response_model=ResponseSchema, status_code = 201)
async def create_category (payload: CategoriesSchema):
    ''' Create a new product '''
    new_category = await service.post(payload)

    response_object = {
        'message': "Category created successfully",
        'data': {
            'category_id': new_category
        }
    }

    return response_object
