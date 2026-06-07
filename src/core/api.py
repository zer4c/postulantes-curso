from fastapi import APIRouter
from src.modules.health.routes import router as router_healt
from src.modules.product.routes import router as router_product


api = APIRouter()

api.include_router(router_healt, prefix="/health-check", tags=["Health"])
api.include_router(router_product, prefix="/product", tags=["Product"])