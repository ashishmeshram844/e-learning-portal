from pydantic import BaseModel
import uuid

class ApiMethodsInput(BaseModel):
    methods : list[str]  

class ApiAvailDataModal(BaseModel):
    id : str
    path : str
    name : str
    summary : str | None  = None
    method : list | None

class ApiListResponse(BaseModel):
    status : int 
    body : list[ApiAvailDataModal]



