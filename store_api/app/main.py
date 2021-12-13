from fastapi import FastAPI
from app.api.v1.routes.products import main as products_routes

app = FastAPI()

app.include_router(products_routes.router)