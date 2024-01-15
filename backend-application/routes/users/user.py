from fastapi import Request
from routes.users.routes import user
from dbs.mongo.queries.user_query import DBQuery
import json
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse
from config.logger.all_loggers import create_user_log_message
import inspect
from routes.users.models import UserInput,UserResponse,UsersListResponse,UpdateUserModel


@user.get('/', response_model = UsersListResponse)
async def get_users(
    request:Request,
    active : bool | None = None
    ) -> UsersListResponse:
    """
    This function get all available users list
    """
    query : dict = {}
    try:
        if active is not None:
            query.update(
                {'active' : active}
                )
        data = DBQuery().find(
            collection='users',
            query=query
        ) 
        return data
    except Exception as e:
        create_user_log_message(
            message=f'failed to get users list because : {e}',
            state="error",
            module=f"{__name__}.{inspect.stack()[0][3]}"
        )
    raise HTTPException(
        status_code=500,
        detail='server connection error'
        )

@user.get('/{user_id}',response_model=UsersListResponse)
async def get_user_detail(
        request:Request,
        user_id : str | None = None
    ) -> UsersListResponse:
    """
    This function get the specific user detail
    """
    data = DBQuery().find(
        collection='users',
        query={'id' : user_id}
    ) 
    try:
        if len(data['body']):
            return data
        else:
            return JSONResponse(
                {
                    'status' : 404,
                    'message' : 'not found',
                    'body' : []
                }
            )
    except Exception as e:
        create_user_log_message(
            message=f'failed to get users detail because : {e}',
            state="error",
            module=f"{__name__}.{inspect.stack()[0][3]}"
        )
    raise HTTPException(
        status_code=500,
        detail='server connection error'
    )

@user.post('/', response_model = UserResponse)
async def create_user(
    request:Request,
    user : UserInput
    ) -> UserResponse:
    """
    This function creates a new user
    """
    try:
        DBQuery().create(
            collection='users',
            data=dict(user)
        )
        return user
    except Exception as e:
        create_user_log_message(
            message=f'failed to create users because : {e}',
            state="error",
            module=f"{__name__}.{inspect.stack()[0][3]}"
        )
    raise HTTPException(
        status_code=500,
        detail='server connection error'
    )

@user.put('/{user_id}',response_model=UsersListResponse)
def update_user(
    request:Request,
    user_id : str,
    update_data : UpdateUserModel
    ):
    try:
        data = DBQuery().update(
            collection='users',
            query= {'id' : user_id},
            update_data=update_data.dict()
        )
        return data
    except Exception as e:
        create_user_log_message(
            message=f'failed to update user because : {e}',
            state="error",
            module=f"{__name__}.{inspect.stack()[0][3]}"
        )
    raise HTTPException(
        status_code=500,
        detail='server connection error'
    )
