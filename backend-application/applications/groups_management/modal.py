"""
Contain all modal which are used in groups  management application
"""

from pydantic import BaseModel
from datetime import datetime
import uuid

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
    permissions : list = []
    created : datetime = datetime.now()
    updated : datetime = datetime.now()
    created_by : str

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





