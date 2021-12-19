from app.database.db import database, categories
from app.models.v2.categories import CategoriesSchema
from fastapi import HTTPException

async def post(category: CategoriesSchema):
    ''' Insert the category into the database '''
    query = categories.insert().values(
        name = category.name,
        description = category.description,
    )

    try:
        await database.connect()
        new_category = await database.execute(query = query)

        await database.disconnect()

        return new_category

    except AssertionError as err:
        raise HTTPException(
            status_code = 500,
            detail = f"An error occurred while creating category on the database: {err}"
        ) from err
