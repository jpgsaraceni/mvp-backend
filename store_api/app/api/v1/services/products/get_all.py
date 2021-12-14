from app.database.db import database
from fastapi import HTTPException

async def get_all():
    ''' Get all existent products from the database '''
    query = "SELECT id, name, description, price, image FROM products WHERE deleted_at IS NULL"

    try:
        await database.connect()
        products = await database.fetch_all(query = query)

        await database.disconnect()

        return products

    except AssertionError as err:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while fetching products from database: {err}"
        ) from err
