from pydantic import BaseModel
from datetime import datetime
import uuid

class GroupsBaseModel(BaseModel):
    name : str

class CreateGroupsModel(GroupsBaseModel):
    id : str = str(uuid.uuid4())
    created : datetime = datetime.now()
    updated : datetime = datetime.now()
    created_by : str

class GroupsListModel(BaseModel):
    status : str
    body : list  = []

class UpdateGroupsModel(BaseModel):
    name : str | None
