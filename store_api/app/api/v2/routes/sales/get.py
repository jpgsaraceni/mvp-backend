from fastapi import APIRouter, HTTPException
from app.api.v2.services.sales import get as service
from app.models.v2.sales import SalesSchemaConsult

router = APIRouter()

@router.get('/sales/{sale_id}', response_model=SalesSchemaConsult, status_code = 200)
async def get_sale_by_id(sale_id: int):
    ''' Get an existent sale by its id '''
    sale = await service.get(sale_id)

    if sale_id < 1:
        raise HTTPException(
            status_code = 400,
            detail = "Sale ID must be greater than 0"
        )

    sale = await service.get(sale_id)

    if not sale:
        raise HTTPException(
            status_code = 404,
            detail = "Sale not found"
        )

    return sale
