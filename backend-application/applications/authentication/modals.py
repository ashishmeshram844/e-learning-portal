"""
This module contain all modal schemas which are required
in token operations
"""

from pydantic import BaseModel, validator
from applications.custom_validators import validate_string_length


class TokenInput(BaseModel):
    """"
    modal uses for genrating token request data
    """
    username : str
    password : str

    @validator('username')
    def validate_username_length(cls,username):
        """
        Check the length of user provided username
        """
        return validate_string_length(
            string = username,
            max_len = 50
        )
    
    @validator('password')
    def validate_password_length(cls,password):
        """
        validate length of user provided password
        """
        return validate_string_length(
            string = password,
            max_len = 80
        )

class TokenResponse(BaseModel):
    """
    Sample modal for token response
    """
    access_token :str
    refresh_token : str

