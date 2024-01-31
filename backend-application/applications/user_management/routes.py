from fastapi import Request, APIRouter,Response,status, Depends
from dbs.mongo.queries.user_query import DBQuery
from fastapi.exceptions import HTTPException
from config.logger.all_loggers import create_user_log_message
import inspect
from applications.authentication.config.jwt import get_hashed_password
from .modals import (
    UsersListResponse, UserResponse, UserInput, 
    UpdateUserModel
)
from .tables import USER_TABLES
from applications.permissions_management.dependencies import check_permission_in_group


user_management = APIRouter(
    prefix= '/users',
    tags= ["User Management"]
)

@user_management.get(
        path='/', 
        response_model = UsersListResponse,
        summary="Get Users List",
    )
async def get_users(
    request:Request,
    response : Response,
    active : bool | None = None,
    # is_permission = Depends(check_permission_in_group)
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
            collection=USER_TABLES.get('users',None),
            query=query
        ) 
        response.status_code = status.HTTP_200_OK
        if not data.get('body',None):
            response.status_code = status.HTTP_200_OK
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


@user_management.get(
        path='/{id}',
        response_model=UsersListResponse,
        summary="Get User Detail"
    )
async def get_user_detail(
        request:Request,
        response : Response,
        id : str | None = None,
    ) :
    """
    ### This function get the specific user detail
    -   fetch a specific user detail as user provided id in path \n
        if user is available  with provided id then return this user \n
        else return not found response
    - #### Path Parameter : 
        - id : (str) - fetch a specific user detail as per id
    """
    data = DBQuery().find(
        collection=USER_TABLES.get('users',None),
        query={'id' : id},
        only_one=True
    )
    try:
        if len(data['body']):
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
            message=f'failed to get users detail because : {e}',
            state="error",
            module=f"{__name__}.{inspect.stack()[0][3]}"
        )
    response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    raise HTTPException(
        status_code=500,
        detail='server connection error'
    )

@user_management.post(
        path='/', 
        response_model = UserResponse,
        summary="Create New User"
    )
async def create_user(
    request:Request,
    response : Response,
    create_data : UserInput
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
        create_data.password = get_hashed_password(create_data.password)
        DBQuery().create(
            collection=USER_TABLES.get('users',None),
            data=dict(create_data)
        )
        response.status_code = status.HTTP_201_CREATED
        return create_data
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

@user_management.put(
        path='/{id}',
        response_model=UsersListResponse,
        summary="Update Role Details"    
    )
def update_user(
    request:Request,
    response : Response,
    id : str,
    update_data : UpdateUserModel
    ) -> UsersListResponse :
    """
    ### This function update the user details
    -   If User provide invalid user id then return not found response
    -   user can update only specific details are mentioned in
        UpdateUserModel
    - #### Path Parameter : 
        - id : (str)
    - #### Body :
        - update_data : (json) - as per UpdateUserModel data includes
    """
    try:
        # for partial update
        update_data = update_data.dict(exclude_unset=True)
        data = DBQuery().update(
            collection=USER_TABLES.get('users',None),
            query= {'id' : id},
            update_data=update_data
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


@user_management.delete(
        path='/{id}',
        summary="Delete User"
    )
def delete_user(
    request:Request,
    response:Response,
    id : str
):
    """
    ### This function delete a specific user 
    -   delete a user which id is provided in path
    -   if id provided in path is not available then return 
        not found response
    -   if deleted successfully then simply return 204 no content
    #### path Parameter : 
        - id : (str) - user id which user want to delete
    """
    try:
        data = DBQuery().delete(
                collection=USER_TABLES.get('users',None),
                query= {'id' : id}
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

