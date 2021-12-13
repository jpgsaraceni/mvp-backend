from app.database.db import database, products
from app.models.v1.products import ProductSchema
from fastapi import HTTPException

async def post(product: ProductSchema):
    ''' Insert the product into the database '''
    query = products.insert().values(
        name = product.name,
        description = product.description,
        price = product.price,
        image = product.image
    )

    try:
        await database.connect()
        new_product = await database.execute(query = query)

        await database.disconnect()

        return new_product

    except AssertionError as err:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while creating product on the database: {err}"
        ) from err
