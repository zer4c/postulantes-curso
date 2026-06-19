from pydantic import BaseModel, ConfigDict, EmailStr

class UserBase(BaseModel):
    name : str
    last_name : str
    old : int
    email: EmailStr

class UserCreate(UserBase):
    password : str

class UserResponse(UserBase):
    model_config = ConfigDict(from_attributes=True)
    id : int

class UserPatch(BaseModel):
    name : str | None = None
    last_name : str | None = None
    old : int | None = None
    password : str | None = None
    email : str | None = None