from datetime import datetime
from pydantic import BaseModel
from typing import Annotated,Optional
from fastapi import Query
from pydantic import Field,validator
from uuid import UUID,uuid4
from pydantic import EmailStr


class UserBase(BaseModel):
    id: str = str(uuid4())
    username : Annotated[str,Query(max_length=55)] 
    mobile : int | None = None 
    email : EmailStr | None = None
    full_name : Annotated[str | None,Query(max_length=100)] = None

class UserInput(UserBase):
    password : Annotated[str,Query(max_length=30)]
    active: bool = True
    created : Optional[datetime] = Field(default=datetime.now())
    updated : Optional[datetime] = Field(default=datetime.now())

class UserResponse(UserBase):
    active: bool
    created :  Optional[datetime | dict]  = Field(default=None)
    updated :  Optional[datetime | dict] = Field(default=None)

class UsersListResponse(BaseModel):
    status : int | str
    body : list[UserResponse]


class UpdateUserModel(BaseModel):
    mobile : Optional[int | str]  
    email : Optional[str] 
    full_name : Optional[str] 
    updated : Optional[datetime | dict]  = Field(default=datetime.now())
