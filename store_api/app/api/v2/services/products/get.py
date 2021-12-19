from fastapi import HTTPException
from sqlalchemy.sql import select
from app.database.db import database, products, categories

async def get(product_id: int):
    ''' Get existent product by id '''
    query = (
        select([
            products.c.name,
            products.c.id,
            products.c.description,
            products.c.price,
            products.c.image,
            products.c.category_id,
            categories.c.name.label('category')
        ])
        .where(
            products.c.id == product_id,
            products.c.deleted_at.is_(None),
            products.c.inactivated_at.is_(None),
            products.c.category_id == categories.c.id
        )
    )

    try:
        await database.connect()
        product = await database.fetch_one(query = query)

        await database.disconnect()

        return product
    except AssertionError as err:
        raise HTTPException(
            status_code = 500,
            detail = f"An error occurred while fetching product from the database: {err}"
        ) from err
