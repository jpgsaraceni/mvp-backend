from fastapi import HTTPException
from sqlalchemy.sql import func
from app.database.db import database, categories
from app.models.v2.categories import CategoriesSchema

async def put(category_id: int, product: CategoriesSchema):
    ''' Update existing product in the database '''
    query = (
        categories
        .update()
        .where(categories.c.id == category_id)
        .values(
            name = product.name,
            description = product.description,
            updated_at = func.now()
        )
        .returning(categories.c.id)
    )

    try:
        await database.connect()
        updated_category = await database.execute(query = query)

        await database.disconnect()

        return updated_category

    except AssertionError as err:
        raise HTTPException(
            status_code = 500,
            detail = f"An error occurred while updating category on the database: {err}"
        ) from err
