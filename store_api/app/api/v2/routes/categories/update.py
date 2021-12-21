from fastapi import APIRouter, HTTPException
from app.models.v2.response import ResponseSchema
from app.models.v2.categories import CategoriesSchema
from app.api.v2.services.categories import put as put_service
from app.api.v2.services.categories import get as get_service

router = APIRouter()

@router.put('/categories/{category_id}', response_model = ResponseSchema, status_code = 202)
async def update_category (category_id: int, payload: CategoriesSchema):
    ''' Update category on the database '''
    if category_id < 1:
        raise HTTPException(status_code=400, detail="Category ID must be greater than 0")

    category = await get_service.get(category_id)

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    category = await put_service.put(category_id, payload)

    response_object = {
        'message': "Category updated successfully",
        'data': {
            'cagetory_id': category
        }
    }

    return response_object
    