from fastapi import APIRouter, HTTPException
from app.models.v2.categories import CategoriesSchemaId
import app.api.v2.services.categories.get as service


router = APIRouter()

@router.get('/categories/{category_id}', response_model=CategoriesSchemaId, status_code = 200)
async def get_category_by_id(category_id: int):
    ''' Get an especific existent product by its ID'''
    if category_id < 1:
        raise HTTPException(status_code=400, detail="Category ID must be greater than 0")

    category = await service.get(category_id)

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    return category
