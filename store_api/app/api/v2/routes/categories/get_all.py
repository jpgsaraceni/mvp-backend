from typing import List
from fastapi import APIRouter
from app.models.v2.categories import CategoriesSchemaId
from app.api.v2.services.categories import get_all as service

router = APIRouter()

@router.get('/categories', response_model=List[CategoriesSchemaId], status_code = 200)
async def get_all_categories ():
    ''' Get all categories from the database '''
    categories = await service.get_all()

    return categories
    