"""
Contain all modals which are required for roles management
"""

from pydantic import BaseModel,validator
from datetime import datetime
import uuid
from applications.custom_validators import (
    check_val_avail,validate_string_length,
    override_uuid,check_id_in_collection
)
from .tables import ROLE_TABLES

class RolesBase(BaseModel):
    """
    Base Modal for roles
    """
    name : str 

class RolesInput(RolesBase):
    """
    This modal used for taking inputs while creating role
    """
    id : str = str(uuid.uuid4())
    created_by : str 
    created : datetime | dict  = datetime.now()
    updated : datetime | dict = datetime.now()

    @validator('id')
    def override_uuid_value(cls,id):
        """
        Override uuid value in request data
        """
        return override_uuid()

    @validator('name')
    def validate_name(cls,name):
        """
        Validate name in request body data 
        - check length 
        - check name is available or not
        """
        validate_string_length(
            string=name,
            max_len=50
        )
        return check_val_avail(
            collection=ROLE_TABLES.get('roles'),
            query=('name',name)
        )


class UpdateRoleModel(BaseModel):
    """
    Used for updating role as modal
    """
    name : str = None

    @validator('name')
    def validate_name(cls,name):
        """
        Validate name in request body data
        - check length of name 
        - check name is available or not
        """
        validate_string_length(
            string=name,
            max_len=50
        )
        return check_val_avail(
            collection=ROLE_TABLES.get('roles'),
            query=('name',name)
        )

class RolesListModel(BaseModel):
    """
    Response Modal for roles list
    """
    status : int
    body : list[RolesInput]



class AssignRoleToUserRequestModal(BaseModel):
    """
    Request model for client to assign roles to a specific user
    """
    role_id : str
    user_id : str

    @validator('role_id')
    def check_role_is_available(cls,role_id):
        """
        Validate the client requested role is available or not
        """
        return check_id_in_collection(
            collection=ROLE_TABLES.get('roles',None),
            query=('id',role_id)
        )

    @validator('user_id')
    def check_user_is_available(cls,user_id):
        """
        Validate client requested user is available or not
        """
        return check_id_in_collection(
            collection=ROLE_TABLES.get('roles',None),
            query=('id',user_id)
        )

