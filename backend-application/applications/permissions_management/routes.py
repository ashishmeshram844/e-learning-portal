from fastapi import APIRouter,Request, Response,status
from dbs.mongo.queries.user_query import DBQuery
from fastapi.exceptions import HTTPException
from .modals import AddPermissionsModal
from .commons import (
    add_permission_in_target,
    update_permission_in_target,
    remove_permission_in_target
)
from .tables import PERMISSIONS_TABLE


permissions_management = APIRouter(
    prefix= '/permissions',
    tags= ["Permission Management"]
)

@permissions_management.post(
        path='/group/add',
        summary="Add Permissions in a Group"
    )
def add_permission_in_group(
    request : Request,
    response : Response,
    update_data : AddPermissionsModal
    ):
    """
    This api remove all previous permissions and add new permissions 
    onlly  which provided in body.
    - Body : 
        - update_data : this contain group id and all permissions list
    """
    try:
        data = add_permission_in_target(
            response=response,
            update_data=update_data,
            target=PERMISSIONS_TABLE.get('groups')
        )
        return data
    except Exception as e:
        ...
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail='server connection error'
    )


@permissions_management.put('/group/update')
def update_permissions_in_groups(
    request : Request,
    response : Response,
    update_data : AddPermissionsModal
    ):
    """
    This api adds the extra permissions in group
    - Body : 
        - update_data : contain group id and list for permissions id
    """
    try:
        data = update_permission_in_target(
            response=response,
            update_data=update_data,
            target=PERMISSIONS_TABLE.get('groups')
        )
        return data
    except Exception as e:
        ...
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail='server connection error'
    )

@permissions_management.delete('/group/remove')
def remove_permissions_in_groups(
    request : Request,
    response : Response,
    update_data : AddPermissionsModal
    ):
    """
    This api removes some permissions from group
    - Body : 
        - update_data : contain group id and list of permissions id
        which we want to remove
    """
    try:
        data = remove_permission_in_target(
            response=response,
            update_data=update_data,
            target=PERMISSIONS_TABLE.get('groups')
        )
        return data
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='server connection error'
        )

@permissions_management.post(
        path='/role/add',
        summary="Add Permissions in a Role"
    )
def add_permission_in_roles(
    request : Request,
    response : Response,
    update_data : AddPermissionsModal
    ):
    """
    This api remove all previous permissions and add new permissions 
    onlly  which provided in body.
    - Body : 
        - update_data : this contain role id and all permissions list
    """
    try:
        data = add_permission_in_target(
            response=response,
            update_data=update_data,
            target=PERMISSIONS_TABLE.get('roles')
        )
        return data
    except Exception as e:
        ...
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail='server connection error'
    )


@permissions_management.put('/role/update')
def update_permissions_in_role(
    request : Request,
    response : Response,
    update_data : AddPermissionsModal
    ):
    """
    This api adds the extra permissions in role
    - Body : 
        - update_data : contain role id and list for permissions id
    """
    try:
        data = update_permission_in_target(
            response=response,
            update_data=update_data,
            target=PERMISSIONS_TABLE.get('roles')
        )
        return data
    except Exception as e:
        ...
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail='server connection error'
    )

@permissions_management.delete('/role/remove')
def remove_permissions_in_role(
    request : Request,
    response : Response,
    update_data : AddPermissionsModal
    ):
    """
    This api removes some permissions from role
    - Body : 
        - update_data : contain role id and list of permissions id
        which we want to remove
    """
    try:
        data = remove_permission_in_target(
            response=response,
            update_data=update_data,
            target=PERMISSIONS_TABLE.get('roles')
        )
        return data
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='server connection error'
        )




