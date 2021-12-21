from app.database.db import database, categories
from fastapi import HTTPException

async def get_all():
    ''' Get all existent categories from the database '''
    query = (
        categories
        .select()
        .where(
            categories.c.deleted_at.is_(None),
            categories.c.inactivated_at.is_(None)
        )
    )

    try:
        await database.connect()
        found_category = await database.fetch_all(query = query)

        await database.disconnect()

        return found_category

    except AssertionError as err:
        raise HTTPException(
            status_code = 500,
            detail = f"An error occurred while fetching categories from database: {err}"
        ) from err
