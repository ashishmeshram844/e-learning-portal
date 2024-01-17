from fastapi import Request
from routes.users.routes import user
from dbs.mongo.queries.user_query import DBQuery
import json
from fastapi.exceptions import HTTPException
from config.logger.all_loggers import create_user_log_message
import inspect
from routes.users.models import *
from fastapi import Response,status
from config.utils import get_hashed_password

@user.get('/', response_model = UsersListResponse)
async def get_users(
    request:Request,
    response : Response,
    active : bool | None = None
    ) -> UsersListResponse:
    """
    ### This function get all available users list.
    -   checks there is active queryparameter is passed or not \n
        if passed then check the value of this and update in query dict\n
        and fetch uses list according to this query dict else fetch \n
        all users list
    - #### Query Parameter : 
        - active : (bool) - fetch users list related to query
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
        response.status_code = status.HTTP_200_OK
        if not data.get('body',None):
            response.status_code = status.HTTP_204_NO_CONTENT
        return data
    except Exception as e:
        create_user_log_message(
            message=f'failed to get users list because : {e}',
            state="error",
            module=f"{__name__}.{inspect.stack()[0][3]}"
        )
    response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    raise HTTPException(
        status_code=500,
        detail='server connection error'
        )

@user.get('/{user_id}',response_model=UsersListResponse)
async def get_user_detail(
        request:Request,
        response : Response,
        user_id : str | None = None
    ) -> UsersListResponse:
    """
    ### This function get the specific user detail
    -   fetch a specific user detail as user provided user_id in path \n
        if user is available  with provided user_id then return this user \n
        else return not found response
    - #### Path Parameter : 
        - user_id : (str) - fetch a specific user detail as per user_id
    """
    data = DBQuery().find(
        collection='users',
        query={'id' : user_id},
        only_one=True
    )
    try:
        if len(data['body']):
            response.status_code = status.HTTP_200_OK
            return data
        else:
            print(data)
            response.status_code = status.HTTP_404_NOT_FOUND
            return {
                    'status' : 404,
                    'body' : []
                }
    except Exception as e:
        create_user_log_message(
            message=f'failed to get users detail because : {e}',
            state="error",
            module=f"{__name__}.{inspect.stack()[0][3]}"
        )
    response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    raise HTTPException(
        status_code=500,
        detail='server connection error'
    )

@user.post('/', response_model = UserResponse)
async def create_user(
    request:Request,
    response : Response,
    user : UserInput
    ) -> UserResponse:
    """
    ### This function creates a new user
    -   username and password are required in body to create a user 
        rest are optional \n
    -   user password is stored in hashed value \n
    -   if user provide invalid data then it shows Unprocessable entity 
    - #### Body :
        - user : (json) - include UserInput model data
    """
    try:
        user.password = get_hashed_password(user.password)
        DBQuery().create(
            collection='users',
            data=dict(user)
        )
        response.status_code = status.HTTP_201_CREATED
        return user
    except Exception as e:
        create_user_log_message(
            message=f'failed to create users because : {e}',
            state="error",
            module=f"{__name__}.{inspect.stack()[0][3]}"
        )
    response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    raise HTTPException(
        status_code=500,
        detail='server connection error'
    )

@user.put('/{user_id}',response_model=UsersListResponse)
def update_user(
    request:Request,
    response : Response,
    user_id : str,
    update_data : UpdateUserModel
    ) -> UsersListResponse :
    """
    ### This function update the user details
    -   If User provide invalid user id then return not found response
    -   user can update only specific details are mentioned in
        UpdateUserModel
    - #### Path Parameter : 
        - user_id : (str)
    - #### Body :
        - update_data : (json) - as per UpdateUserModel data includes
    """
    try:
        data = DBQuery().update(
            collection='users',
            query= {'id' : user_id},
            update_data=update_data.dict()
        )
        if data.get("body",None):
            response.status_code = status.HTTP_200_OK
            return data
        else:
            response.status_code = status.HTTP_404_NOT_FOUND
            return {
                    'status' : 404,
                    'body' : []
                }
    except Exception as e:
        create_user_log_message(
            message=f'failed to update user because : {e}',
            state="error",
            module=f"{__name__}.{inspect.stack()[0][3]}"
        )
    response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    raise HTTPException(
        status_code=500,
        detail='server connection error'
    )


@user.delete('/{user_id}')
def delete_user(
    request:Request,
    response:Response,
    user_id : str
):
    """
    ### This function delete a specific user 
    -   delete a user which user_id is provided in path
    -   if user_id provided in path is not available then return 
        not found response
    -   if deleted successfully then simply return 204 no content
    #### path Parameter : 
        - user_id : (str) - user id which user want to delete
    """
    try:
        data = DBQuery().delete(
                collection='users',
                query= {'id' : user_id}
            )
        if not data.get('status',None) == 404:
            response.status_code = status.HTTP_204_NO_CONTENT
        else:
            response.status_code = status.HTTP_404_NOT_FOUND
        return data
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        raise HTTPException(
            status_code=500,
            detail='server connection error'
        )

