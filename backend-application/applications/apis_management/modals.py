"""
Contain all modals which are required for apis managements
"""

from pydantic import BaseModel
import uuid
from enum import Enum
from pydantic import validator


class AvailableApiMethods(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    HEAD = "HEAD"

class ApiMethodsInput(BaseModel):
    """
    Basemodal for Api methods data
    """
    methods : list[str]  

    @validator('methods')
    def check_methods_avail(cls,methods):
        """
        This validate the requested api method is valid or not as per
        our requirements
        """
        for parsed_method in methods:
            if not parsed_method.upper() in AvailableApiMethods.__members__:
                raise  ValueError(f"{parsed_method} method is invalid")
        return methods

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

