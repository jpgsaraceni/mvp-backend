from fastapi import HTTPException
from app.database.db import database, categories

async def get(category_id: int):
    ''' Get existent category by id '''
    query = (
        categories
        .select()
        .where(
            categories.c.id == category_id,
            categories.c.deleted_at.is_(None),
            categories.c.inactivated_at.is_(None),
        )
    )

    try:
        await database.connect()
        category = await database.fetch_one(query = query)

        await database.disconnect()

        return category
    except AssertionError as err:
        raise HTTPException(
            status_code = 500,
            detail = f"An error occurred while fetching category from the database: {err}"
        ) from err
