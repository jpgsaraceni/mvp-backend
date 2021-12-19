from fastapi import APIRouter, HTTPException
from app.models.v2.response import ResponseSchema
from app.api.v2.services.sales import delete as delete_service
from app.api.v2.services.sales import get as get_service

router = APIRouter()

@router.delete('/sales/{sale_id}', response_model=ResponseSchema, status_code = 200)
async def delete_sale(sale_id: int):
    ''' Delete existent sale '''
    if sale_id < 1:
        raise HTTPException(
            status_code = 400,
            detail = "The sale ID bust be greater than 0"
        )

    sale = await get_service.get(sale_id)

    if not sale:
        raise HTTPException(
            status_code = 404,
            detail = "Sale not found"
        )

    deleted_sale = await delete_service.delete(sale_id)

    response_object = {
        'message': "Sale deleted successfully",
        'data': {
            'sale_id': deleted_sale
        }
    }

    return response_object
