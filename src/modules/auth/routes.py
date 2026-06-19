from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends
from src.core.database import SessionDep
from src.modules.auth.controller import AuthController

router = APIRouter()


@router.post("/auth")
async def login(
    session: SessionDep, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    return await AuthController.login(session, form_data)

