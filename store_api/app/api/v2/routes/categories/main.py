from fastapi import APIRouter
from app.api.v2.routes.categories import create as create_category
from app.api.v2.routes.categories import get as get_category
from app.api.v2.routes.categories import get_all as get_all_categories
from app.api.v2.routes.categories import update as update_category
from app.api.v2.routes.categories import delete as delete_category

router = APIRouter(
    tags=["categories"]
)

router.include_router(create_category.router)
router.include_router(get_category.router)
router.include_router(get_all_categories.router)
router.include_router(update_category.router)
router.include_router(delete_category.router)
