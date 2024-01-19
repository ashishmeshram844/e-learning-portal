from pydantic import BaseModel
from datetime import datetime
import uuid


class PermissionBaseModel(BaseModel):
    name : str

class CreatePermissionModel(PermissionBaseModel):
    id : str = str(uuid.uuid4())
    created : datetime = datetime.now()
    updated : datetime = datetime.now()
    created_by : str


class PermissionsListModel(BaseModel):
    status : str
    body : list  = []



class UpdatePermissionModel(BaseModel):
    name : str | None
