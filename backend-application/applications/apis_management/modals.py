"""
Contain all modals which are required for apis managements
"""

from pydantic import BaseModel
import uuid
from enum import Enum
from pydantic import validator
#from applications.user_management.validators import validate_string_length
from .common import *



class AvailableApiMethods(Enum):
    """
    List of methods which are allowed
    following methods can only request user 
    """
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    HEAD = "HEAD"

class ApiMethodsInput(BaseModel):
    """
    Input request modal for client for fetchig apis list
    """
    methods : list[str]  

    @validator('methods')
    def check_methods_avail(cls,methods):
        """
        This validate the requested api method is valid or not as per
        our requirements
        """
        for parsed_method in methods:
            validate_string_length(
                string = parsed_method,
                max_len = 6
            )
            if not parsed_method.upper() in AvailableApiMethods.__members__:
                raise  ValueError(f"{parsed_method} method is invalid")
        return methods

class ApiAvailDataModal(BaseModel):
    """
    Modal for Response available api data
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

