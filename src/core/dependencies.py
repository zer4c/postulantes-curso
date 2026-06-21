from typing import Annotated

import jwt
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException
from src.core.database import SessionDep
from src.core.config import config
from src.modules.user.services import UserService
from src.modules.user.schemas import UserResponse
from src.core.enums import TypeRoles

tokenBearer = OAuth2PasswordBearer(tokenUrl="/auth/token")
tokenDep = Annotated[str, Depends(tokenBearer)]


async def authenticate(token: tokenDep, session: SessionDep):
    try:
        payload = jwt.decode(token,config.secret_key, algorithms=[config.algorithm])
        subject = payload["sub"]
        user = await UserService.get_by_email(subject, session)
        if not user:
            raise HTTPException(
                status_code=404, detail="user not founded"
            )
        return user
    except Exception as e:
        raise e

CurrentUser = Annotated[UserResponse,Depends(authenticate)]

def validate_admin(user :CurrentUser):
    if user.role != TypeRoles.ADMIN:
        raise HTTPException(status_code=401, detail="user not admin")