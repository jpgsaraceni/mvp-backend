from fastapi import HTTPException
from app.database.db import database, products

async def get(product_id: int):
    ''' Get existent product by id '''
    query = (
        products
        .select()
        .where(
            products.c.deleted_at.is_(None),
            products.c.id == product_id
        )
    )

    try:
        await database.connect()
        product = await database.fetch_one(query = query)

        await database.disconnect()

        return product
    except AssertionError as err:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while fetching product from the database: {err}"
        ) from err
