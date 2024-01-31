"""
Contain all modals which are required for roles management
"""

from pydantic import BaseModel
from datetime import datetime
import uuid

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


class UpdateRoleModel(BaseModel):
    """
    Used for updating role as modal
    """
    name : str = None


class RolesListModel(BaseModel):
    """
    Response Modal for roles list
    """
    status : int
    body : list[RolesInput]



class AssignRoleToUserRequestModal(BaseModel):
    role_id : str
    user_id : str