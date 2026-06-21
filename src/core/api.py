from fastapi import APIRouter
from src.modules.health.routes import router as router_healt
from src.modules.product.routes import router as router_product
from src.modules.auth.routes import router as router_auth
from src.modules.user.routes import router as router_user

api = APIRouter()

api.include_router(router_auth , prefix="/auth", tags=["Auth"])
api.include_router(router_user, prefix="/user", tags=["User"])
api.include_router(router_healt, prefix="/health-check", tags=["Health"])
api.include_router(router_product, prefix="/product", tags=["Product"])