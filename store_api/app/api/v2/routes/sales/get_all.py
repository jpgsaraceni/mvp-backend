from typing import List
from fastapi import APIRouter
from app.models.v2.sales import SalesSchemaConsult
import app.api.v2.services.sales.get_all as service

router = APIRouter()

@router.get('/sales', response_model=List[SalesSchemaConsult], status_code = 200)
async def get_all_sales(
    category: int = None,
    product: int = None,
    client: int = None,
    payment_method: int = None
):
    ''' List all existent sales \n
        The sales can be filter by: \n
        category: Product category id \n
        product: Product id \n
        payment_method: Payment method id \n
        client: Client id \n
    '''
    sales = await service.get_all(
        category = category,
        product = product,
        client = client,
        payment_method = payment_method
    )

    return sales
