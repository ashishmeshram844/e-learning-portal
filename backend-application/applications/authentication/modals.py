"""
This module contain all modal schemas which are required
in token operations
"""

from pydantic import BaseModel


class TokenInput(BaseModel):
    """"
    modal uses for genrating token request data
    """
    username : str
    password : str


class TokenResponse(BaseModel):
    """
    Sample response modal for token response 
    """
    access_token :str
    refresh_token : str

