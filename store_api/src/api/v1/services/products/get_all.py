from app.database.db import database, products
from fastapi import HTTPException

async def get_all():
    ''' Get all existent products from the database '''
    query = (
        products
        .query()
        .with_entities(
            products.c.id,
            products.c.name,
            products.c.description,
            products.c.price,
        )
        .where(products.c.deleted_at is not None)
    )

    try:
        await database.connect()
        found_products = await database.fetch_all(query = query)

        await database.disconnect()

        return found_products

    except AssertionError as err:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while fetching products from database: {err}"
        ) from err
