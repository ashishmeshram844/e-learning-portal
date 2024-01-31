"""
All modals related to Users
- client request modals
- client response modals
"""
from datetime import datetime
from pydantic import BaseModel,validator
from typing import Annotated,Optional
from fastapi import Query
from pydantic import Field
from uuid import uuid4
from pydantic import EmailStr
from .tables import USER_TABLES
from .validators import check_val_avail,convert_miliseconds_to_time


class UserBase(BaseModel):
    """
    Base modal for user data fields
    """
    id: str = str(uuid4())
    username : Annotated[str,Query(
        max_length=55
        )] 
    mobile : int | None = None 
    email : EmailStr | None = None
    full_name : Annotated[str | None,Query(
        max_length=100
        )] = None
    
class UserInput(UserBase):
    """
    Model for client request User creation  data
    """
    password : Annotated[str,Query(
        max_length=30
        )]
    active: bool = True
    created : Optional[datetime] = Field(
        default=datetime.now()
        )
    updated : Optional[datetime] = Field(
        default=datetime.now()
        )
    
    @validator('username')
    def check_username_avail(cls,username):
        """
        checks username is already registered or not
        """
        return check_val_avail(
            collection=USER_TABLES.get('users'),
            query=('username',username),
        )
    
    @validator('email')
    def check_email_avail(cls,email):
        """
        Check email is already registered or not
        """
        return check_val_avail(
            collection=USER_TABLES.get('users'),
            query=('email',email),
        )
    
    @validator('mobile')
    def check_mobile_avail(cls,mobile):
        """
        Check mobile number is already available in user
        database or not
        """
        return check_val_avail(
            collection=USER_TABLES.get('users'),
            query=('mobile',mobile),
        )


class UserResponse(UserBase):
    """
    Sample response model for Users data
    inherit the fields from UserBase class Modal
    """
    active: bool
    created :  Optional[datetime | dict]  = Field(
        default=None
        )
    updated :  Optional[datetime | dict] = Field(
        default=None
        )
    
    @validator('created')
    def deserialize_created_date(cls,created):
        """
        Converts created datetime object to proper datetime format
        """
        try:
            return convert_miliseconds_to_time(
                date_obj=created
            )
        except:
            return created
        
    @validator('updated')
    def deserialize_updated_date(cls,updated):
        """
        Convert updated datetime object to proper datetime format
        """
        try:
            return convert_miliseconds_to_time(
                date_obj=updated
            )
        except:
            return updated
   
class UsersListResponse(BaseModel):
    """
    User request modal for response of Users list
    """
    status : int | str
    body : list[UserResponse]


class UpdateUserModel(BaseModel):
    """
    This modal is used to validate user update schema 
    from client request
    """
    mobile : Optional[int | str]  
    email : Optional[str] 
    full_name : Optional[str] 
    role : str | None = None
    updated : Optional[datetime | dict]  = Field(
        default=datetime.now()
        )

    @validator('email')
    def check_email_avail(cls,email):
        """
        Check email is already registered or not
        """
        return check_val_avail(
            collection=USER_TABLES.get('users'),
            query=('email',email),
        )
    
    @validator('mobile')
    def check_mobile_avail(cls,mobile):
        """
        Check mobile number is already available in user
        database or not
        """
        return check_val_avail(
            collection=USER_TABLES.get('users'),
            query=('mobile',mobile),
        )