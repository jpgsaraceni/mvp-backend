from datetime import datetime, timedelta
from fastapi import HTTPException
from app.database.db import database, sales
from app.models.v2.sales import SalesSchema

async def post (sale: SalesSchema):
    ''' Insert the sale into the database '''

    end_date = datetime or None

    if sale.valid_for != 0:
        end_date = datetime.now() + timedelta(days = sale.valid_for)
    else:
        end_date = None

    query = (
        sales
        .insert()
        .values(
            client_id = sale.client_id,
            product_id = sale.product_id,
            payment_method_id = sale.payment_method_id,
            amount = sale.amount,
            price = sale.price,
            valid_until = end_date
        )
    )

    try:
        await database.connect()

        sale_id = await database.execute(query = query)

        await database.disconnect()

        return sale_id

    except AssertionError as err:
        raise HTTPException(
            status_code=500,
            detail=f'An error occurred while creating sale on the database: {err}'
        ) from err
