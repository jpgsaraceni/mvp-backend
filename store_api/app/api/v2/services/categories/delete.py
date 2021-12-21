from fastapi import HTTPException
from sqlalchemy.sql import func
from app.database.db import database, categories
from app.api.v2.services.products import get_all as service

async def delete(category_id: int):
    ''' Delete existing product in the database '''
    used_category = await service.get_all(category = category_id)

    if len(used_category) == 0:
        query = (
            categories
            .update()
            .where(categories.c.id == category_id)
            .values(
                deleted_at = func.now()
            )
            .returning(categories.c.id)
        )
    else:
        query = (
            categories
            .update()
            .where(categories.c.id == category_id)
            .values(
                inactivated_at = func.now()
            )
            .returning(categories.c.id)
        )

    try:
        await database.connect()
        deleted_category = await database.execute(query = query)

        await database.disconnect()

        return deleted_category

    except AssertionError as err:
        raise HTTPException(
            status_code = 500,
            detail = f"An error occurred while deleting category from the database: {err}"
        ) from err
