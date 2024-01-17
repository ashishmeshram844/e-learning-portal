from fastapi import FastAPI, status, HTTPException, Depends
from fastapi.responses import RedirectResponse
from routes.users.routes import auth
from config.utils import (
    get_hashed_password,
    create_access_token,
    create_refresh_token,
    verify_password
)
from commons.responses import ERR_RESPONSES

from routes.users.models import LoginModel
from dbs.mongo.queries.user_query import DBQuery
from routes.users.models import TokenModel


@auth.post('/token', response_model=TokenModel)
async def create_token(form_data:LoginModel):
    try:
        user = DBQuery().find(
            collection='users',
            query={'username': form_data.username},
            only_one=True
        ) 
        print("SAS" ,user)  
        if not user.get('status',None) == 200:
            return ERR_RESPONSES.get(401,500)
        if not user.get('body'):
            return ERR_RESPONSES.get(401,500)
        hashed_pass = user.get('body')[0].get('password')
        if not verify_password(form_data.password, hashed_pass):
            return ERR_RESPONSES.get(401,500)
        return {
            "access_token": create_access_token(user.get('body')[0].get('username')),
            "refresh_token": create_refresh_token(user.get('body')[0].get('username')),
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail='server connection error'
            )




# @auth.post('/signup', summary="Create new user", response_model=UserOut)
# async def create_user(data: UserAuth):
#     # querying database to check if user already exist
#     user = db.get(data.email, None)
#     if user is not None:
#             raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail="User with this email already exist"
#         )
#     user = {
#         'email': data.email,
#         'password': get_hashed_password(data.password),
#         'id': str(uuid4())
#     }
#     db[data.email] = user    # saving user to database
#     return user




