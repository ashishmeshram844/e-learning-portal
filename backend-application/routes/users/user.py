from fastapi import Request
from routes.users.routes import user
from dbs.mongo.queries.user_query import find,create
import json
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse
from config.logger.all_loggers import create_user_log_message
import inspect
from routes.users.models import UserInput,UserResponse,UsersListResponse


@user.get('/', 
          response_model = UsersListResponse
        )
async def get_users(
    request:Request,
    active : bool | None = None
    ) -> UsersListResponse:
    query = {}
    if active is not None:
        query.update({'active' : active})
    try:
        data = find(collection='users',query=query) 
        return data
    except Exception as e:
        create_user_log_message(
            message=f'failed to get users list because : {e}',
            state="error",
            module=f"{__name__}.{inspect.stack()[0][3]}"
        )
        raise HTTPException(status_code=500,detail='server connection error')

@user.post('/',
           response_model = UserResponse
        )
async def create_user(
    request:Request,
    user : UserInput
    ) -> UserResponse:
    try:
        create(collection='users',data=dict(user))
        return user
    except Exception as e:
        create_user_log_message(
            message=f'failed to create users because : {e}',
            state="error",
            module=f"{__name__}.{inspect.stack()[0][3]}"
        )
    raise HTTPException(status_code=500,detail='server connection error')
    

