from pydantic import BaseModel, ConfigDict, EmailStr
from src.core.enums import TypeRoles


class UserBase(BaseModel):
    name: str
    last_name: str
    old: int
    email: EmailStr


class UserCreate(UserBase):
    password: str
    role: TypeRoles | None = TypeRoles.USER


class UserResponse(UserBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    role: TypeRoles


class UserPatch(BaseModel):
    name: str | None = None
    last_name: str | None = None
    old: int | None = None
    password: str | None = None
    email: str | None = None
