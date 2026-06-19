from pydantic import BaseModel, ConfigDict

class UserBase(BaseModel):
    name : str
    last_name : str
    old : int

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    model_config = ConfigDict(from_attributes=True)
    id : int

class UserPatch(BaseModel):
    name : str | None = None
    last_name : str | None = None
    old : int | None = None