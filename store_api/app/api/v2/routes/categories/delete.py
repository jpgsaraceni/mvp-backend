from fastapi import APIRouter, HTTPException
from app.models.v2.response import ResponseSchema
from app.api.v2.services.categories import get as get_service
from app.api.v2.services.categories import delete as delete_service

router = APIRouter()

@router.delete('/categories/{category_id}',response_model=ResponseSchema, status_code = 200)
async def delete_category (category_id: int):
    ''' Delete a category from the database '''
    if category_id < 1:
        raise HTTPException (
            status_code = 400,
            detail = "The category id must be greater than 0"
        )

    category =  await get_service.get(category_id)

    if not category:
        raise HTTPException (
            status_code = 404,
            detail = "Category not found"
        )

    deleted_category = await delete_service.delete(category_id)

    response_object = {
        'message': "Category deleted successfully",
        'data': {
            'category_id': deleted_category
        }
    }

    return response_object
    