from fastapi import APIRouter
from app.api.v2.routes.products import main as products_routes
from app.api.v2.routes.categories import main as categories_routes

router = APIRouter(
    prefix='/v2',
    tags=["v2"]
)

router.include_router(products_routes.router)
router.include_router(categories_routes.router)
