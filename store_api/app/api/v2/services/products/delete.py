from fastapi import HTTPException
from sqlalchemy.sql import func
from app.database.db import database, products
from app.api.v2.services.sales import get_all as service

async def delete(product_id: int):
    ''' Delete existing product in the database '''
    sold_product = await service.get_all(product = product_id)

    if len(sold_product) == 0:
        query = (
            products
            .update()
            .where(products.c.id == product_id)
            .values(
                deleted_at = func.now()
            )
            .returning(products.c.id)
        )
    else:
        query = (
            products
            .update()
            .where(products.c.id == product_id)
            .values(
                inactivated_at = func.now()
            )
            .returning(products.c.id)
        )

    try:
        await database.connect()
        deleted_product = await database.execute(query = query)

        await database.disconnect()

        return deleted_product

    except AssertionError as err:
        raise HTTPException(
            status_code = 500,
            detail = f"An error occurred while deleting product from the database: {err}"
        ) from err
