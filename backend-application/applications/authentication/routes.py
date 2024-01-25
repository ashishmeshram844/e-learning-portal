"""
Contains all authentications related apis 
- JWT Token is used
- token generations
- get user from token
"""

from fastapi import (
    Request, Response, status, 
    APIRouter, HTTPException, Depends
    )
from dbs.mongo.queries.user_query import DBQuery
from .tables import AUTH_TABLES
from .config.jwt import (
    create_access_token,
    create_refresh_token,
    verify_password
)
from .modals import TokenInput, TokenResponse
from .dependencies import get_current_user

authentication = APIRouter(
    prefix= '/auth',
    tags= ["Authentication"]
)

@authentication.post(
        path= '/token',
        response_model=TokenResponse,
        summary="Generate JWT Token"
        )
async def create_token(
    request : Request,
    response : Response,
    body_data:TokenInput,
    ):
    """
    This api creates a token for user authentication
    - Body : 
        - username : str
        - password : str
    """
    try:
        user = DBQuery().find(
            collection=AUTH_TABLES.get('users',None),
            query={'username': body_data.username},
            only_one=True
        ) 
        if not user.get('status',None) == 200:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='failed to authenticate'
            )
        if not user.get('body',None):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="not found"
            )
        hashed_pass = user.get('body')[0].get('password')
        if not verify_password(
            body_data.password, 
            hashed_pass
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='failed to authenticate'
            )
        response.status_code = status.HTTP_201_CREATED
        return {
            "access_token": create_access_token(
                user.get('body')[0].get('username')
            ),
            "refresh_token": create_refresh_token(
                user.get('body')[0].get('username')
            )
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='server connection error'
            )



@authentication.get(
        path='/me',
        summary="Get Token Detail"
    )
async def get_token_user(
    request : Request,
    user = Depends(get_current_user)):
    """
    This function return the current user details which token
    is provided in header
    """
    try:
        return user
    except Exception as e:
        print(e)
        return {}
    
    