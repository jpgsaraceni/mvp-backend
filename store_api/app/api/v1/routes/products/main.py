from fastapi import APIRouter
from app.api.v1.routes.products import create as create_product
from app.api.v1.routes.products import update as update_product
from app.api.v1.routes.products import delete as delete_product
from app.api.v1.routes.products import get as get_product
from app.api.v1.routes.products import get_all as get_all_products

router = APIRouter(
    prefix='/v1',
    tags=["v1", "products"]
)

router.include_router(create_product.router)
router.include_router(get_all_products.router)
router.include_router(get_product.router)
router.include_router(update_product.router)
router.include_router(delete_product.router)
