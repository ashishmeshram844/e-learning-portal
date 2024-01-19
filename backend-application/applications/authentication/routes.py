from fastapi import (
    Request, Response, status, 
    APIRouter, HTTPException, Depends
    )
from dbs.mongo.queries.user_query import DBQuery
from .tables import AUTH_TABLES
from .config.jwt import (
    get_hashed_password,
    create_access_token,
    create_refresh_token,
    verify_password
)
from .modals import TokenInput, TokenResponse
from .dependencies import get_current_user

auth = APIRouter(
    prefix= '/auth',
    tags= ["Authentication"]
)

@auth.post('/token',response_model=TokenResponse)
async def create_token_from_auth(
    request : Request,
    response : Response,
    body_data:TokenInput
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



@auth.get('/me')
async def get_me(
    request : Request,
    user = Depends(get_current_user)):
    try:
        return user
    except Exception as e:
        print(e)
        return {}
    
    