from app.database.db import database, products
from fastapi import HTTPException

async def get_all():
    ''' Get all existent products from the database '''
    query = (
        products
        .select()
        .where(products.c.deleted_at is not None)
    )

    try:
        await database.connect()
        found_product = await database.fetch_all(query = query)

        await database.disconnect()

        return found_product

    except AssertionError as err:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while fetching products from database: {err}"
        ) from err
