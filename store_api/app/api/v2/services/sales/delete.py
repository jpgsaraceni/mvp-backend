from fastapi import HTTPException
from sqlalchemy.sql import func
from app.database.db import database, sales

async def delete(sale_id: int):
    ''' Delete existing sale in the database '''
    query = (
        sales
        .update()
        .where(
            sales.c.id == sale_id
        )
        .values(
            deleted_at = func.now()
        )
        .returning(sales.c.id)
    )

    try:
        await database.connect()
        deleted_product = await database.execute(query = query)

        await database.disconnect()

        return deleted_product

    except AssertionError as err:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while deleting sale from the database: {err}"
        ) from err
