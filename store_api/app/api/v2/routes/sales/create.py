from fastapi import APIRouter, HTTPException
from app.models.v2.sales import SalesSchema
from app.models.v2.response import ResponseSchema
from app.api.v2.services.sales import post as service
from app.api.v2.services.products import get as products_service

router = APIRouter()

@router.post('/sales', response_model=ResponseSchema, status_code=202)
async def create_sale (payload: SalesSchema):
    ''' Create a new sale \n
        The valid_for field is the number of days a sale is valid.
        For a lifetime sale, ignore this field or set its value to 0
    '''
    product = await products_service.get(payload.product_id)

    if not product:
        raise HTTPException (
            status_code = 404,
            detail = "Product not found"
        )

    new_sale = await service.post(payload)

    response_object = {
        'message': "Sale created successfully",
        'data': {
            'sale_id': new_sale
        }
    }

    return response_object
