from pydantic import BaseModel


class ApiMethodsInput(BaseModel):
    methods : list | None 

class ApiAvailDataModal(BaseModel):
    path : str
    name : str
    summary : str | None  = None
    method : list | None

class ApiListResponse(BaseModel):
    status : int 
    body : list[ApiAvailDataModal]
