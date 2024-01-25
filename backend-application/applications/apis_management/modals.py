"""
Contain all modals which are required for apis managements
"""

from pydantic import BaseModel
import uuid

class ApiMethodsInput(BaseModel):
    """
    Basemodal for Api methods data
    """
    methods : list[str]  

class ApiAvailDataModal(BaseModel):
    """
    Modal fgr Response available api data
    """
    id : str
    path : str
    name : str
    summary : str | None  = None
    method : list | None

class ApiListResponse(BaseModel):
    """
    Response modal for apis lists
    """
    status : int 
    body : list[ApiAvailDataModal]



