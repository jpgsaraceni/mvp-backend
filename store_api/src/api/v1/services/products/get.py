from fastapi import HTTPException
from app.database.db import database, products

async def get(product_id: int):
    ''' Get existent product by id '''
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
        product = await database.fetch_one(query = query, values = {'id': product_id})

        await database.disconnect()

        return product
    except AssertionError as err:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while fetching product from the database: {err}"
        ) from err
