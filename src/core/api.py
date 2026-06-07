from fastapi import APIRouter
from src.modules.health.routes import router as router_healt


api = APIRouter()

api.include_router(router_healt, prefix="/health-check", tags=["Health"])