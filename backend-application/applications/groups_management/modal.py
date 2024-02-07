"""
Contain all modal which are used in groups  management application
"""

from pydantic import BaseModel
from datetime import datetime
import uuid
from pydantic import validator
from .tables import GROUPS_TABLE
from applications.user_management.validators import check_val_avail

class GroupsBaseModel(BaseModel):
    """
    This is base modal for groups
    """
    name : str


class CreateGroupsModel(GroupsBaseModel):
    """
    Modal used when creating group 
    - equest data as per this modal while creating group
    """
    id : str = str(uuid.uuid4())
    created : datetime = datetime.now()
    updated : datetime = datetime.now()
    created_by : str

    @validator('name')
    def check_group_is_avail(cls,name):
         return check_val_avail(
            collection=GROUPS_TABLE.get('groups'),
            query=('name',name),
        )

class GroupsListModel(BaseModel):
    """
    Sample response modal for groups
    """
    status : str
    body : list  = []

class UpdateGroupsModel(BaseModel):
    """
    Update group modal 
    - can update only this modal fields in group
    """
    name : str | None





