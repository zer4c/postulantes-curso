from fastapi import APIRouter
from src.modules.health.controllers import ControllerHealth

router = APIRouter()

@router.get("/")
def healt_check():
    return ControllerHealth.healt_check()