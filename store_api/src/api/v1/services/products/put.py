from fastapi import HTTPException
from sqlalchemy.sql import func
from app.database.db import database, products
from app.models.v1.products import ProductSchema

async def put(product_id: int, product: ProductSchema):
    ''' Update existing product in the database '''
    query = (
        products
        .update()
        .where(products.c.id == product_id)
        .values(
            name=product.name,
            description=product.description,
            price=product.price,
            image=product.image,
            updated_at=func.now()
        )
        .returning(products.c.id)
    )

    try:
        await database.connect()
        updated_product = await database.execute(query=query)

        await database.disconnect()

        return updated_product

    except AssertionError as err:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while updating product on the database: {err}"
        ) from err
