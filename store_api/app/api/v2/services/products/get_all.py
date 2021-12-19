from app.database.db import database, products, categories
from fastapi import HTTPException
from sqlalchemy.sql import select

async def get_all(
    category: int = None
):
    ''' Get all existent products from the database '''
    query = (
        select(
            [
                products.c.name,
                products.c.price,
                products.c.description,
                products.c.id,
                products.c.image,
                products.c.category_id,
                categories.c.name.label('category')
            ]
        )
        .where(
            products.c.deleted_at.is_(None),
            products.c.inactivated_at.is_(None),
            products.c.category_id == categories.c.id
        )
    )

    if category is not None:
        query.append_whereclause(products.c.category_id == category)

    try:
        await database.connect()
        found_product = await database.fetch_all(query = query)

        await database.disconnect()

        return found_product

    except AssertionError as err:
        raise HTTPException(
            status_code = 500,
            detail = f"An error occurred while fetching products from database: {err}"
        ) from err
