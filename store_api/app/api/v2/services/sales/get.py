from fastapi import HTTPException
from app.database.db import database, sales

async def get(sale_id: int):
    ''' Get existent sale by id '''
    query = (
        sales
        .select()
        .where(
            sales.c.id == sale_id,
            sales.c.deleted_at.is_(None),
        )
    )

    try:
        await database.connect()
        sale = await database.fetch_one(query = query)

        await database.disconnect()

        return sale
    except AssertionError as err:
        raise HTTPException(
            status_code = 500,
            detail = f"An error occurred while fetching sale from the database: {err}"
        ) from err
