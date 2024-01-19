from pydantic import BaseModel
from datetime import datetime
import uuid

class RolesBase(BaseModel):
    name : str 

class RolesInput(RolesBase):
    id : str = str(uuid.uuid4())
    created_by : str 
    created : datetime | dict  = datetime.now()
    updated : datetime | dict = datetime.now()


class UpdateRoleModel(BaseModel):
    name : str = None


class RolesListModel(BaseModel):
    status : int
    body : list[RolesInput]