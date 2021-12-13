from fastapi import HTTPException
from app.database.db import database

async def get(product_id: int):
    ''' Get existent product by id '''
    query = '''SELECT id,
        name,
        description,
        price,
        image
        FROM products WHERE deleted_at IS NULL AND id = :id'''

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
