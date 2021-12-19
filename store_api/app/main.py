from fastapi import FastAPI
from app.api.v1.routes.products import main as v1_routes
from app.api.v2.routes import main as v2_routes

app = FastAPI()

app.include_router(v1_routes.router)

app.include_router(v2_routes.router)
