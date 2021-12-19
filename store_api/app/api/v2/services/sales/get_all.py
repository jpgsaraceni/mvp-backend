from fastapi import HTTPException
from app.database.db import database, sales, products
from sqlalchemy.sql import select

async def get_all(
    product: int = None,
    category: int = None,
    payment_method: int = None,
    client: int = None
):
    ''' Get all existent sales from the database '''
    query = (
        select(
            [
                sales.c.id,
                sales.c.client_id,
                sales.c.product_id,
                sales.c.payment_method_id,
                sales.c.amount,
                sales.c.price,
                sales.c.valid_until,
                sales.c.created_at
            ]
        )
        .where(
            sales.c.deleted_at.is_(None),
        )
    )

    if product is not None:
        query.append_whereclause(sales.c.product_id == product)

    if payment_method is not None:
        query.append_whereclause(sales.c.payment_method_id == payment_method)

    if client is not None:
        query.append_whereclause(sales.c.client_id == client)

    if category is not None:
        query.append_whereclause(sales.c.product_id == products.c.id)
        query.append_whereclause(products.c.category_id == category)

    try:
        await database.connect()
        found_product = await database.fetch_all(query = query)

        await database.disconnect()

        return found_product

    except AssertionError as err:
        raise HTTPException(
            status_code = 500,
            detail = f"An error occurred while fetching sales from database: {query}"
        ) from err
