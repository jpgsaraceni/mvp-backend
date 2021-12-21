from fastapi import APIRouter
from app.api.v2.routes.sales import create as create_sale
from app.api.v2.routes.sales import get_all as get_all_sales
from app.api.v2.routes.sales import get as get_sales
from app.api.v2.routes.sales import delete as delete_sales

router = APIRouter(
    tags=["sales"]
)

router.include_router(create_sale.router)
router.include_router(get_all_sales.router)
router.include_router(get_sales.router)
router.include_router(delete_sales.router)
