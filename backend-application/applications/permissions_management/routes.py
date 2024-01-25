from fastapi import APIRouter,Request, Response,status
from dbs.mongo.queries.user_query import DBQuery
from fastapi.exceptions import HTTPException
from applications.groups_management.tables import GROUPS_TABLE
from .modals import AddPermissionsInGroupModal
from .commons import add_permission, update_permission


permissions_management = APIRouter(
    prefix= '/permission',
    tags= ["Permission Management"]
)



@permissions_management.post(
        path='/permissions/group/add',
        summary="Add Permissions in a Group"
    )
def add_permission_in_group(
    request : Request,
    response : Response,
    update_data : AddPermissionsInGroupModal
    ):
    """
    This api remove all previous permissions and add new permissions 
    onlly  which provided in body.
    - Body : 
        - update_data : this contain group id and all permissions list
    """
    try:
        update_data = update_data.dict(exclude_unset=True)
        api_permissions_ids = update_data.get('api_permissions')
        if not api_permissions_ids:
            response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
            return {
                'status' : 422,
                'message' : "permissions object not provided"
            }
        api_objects = DBQuery().find(
            collection=GROUPS_TABLE.get('apis'),
            query={"id" : {"$in" : api_permissions_ids}}
        )
        if not api_objects.get('body'):
            return {
                'status' : status.HTTP_404_NOT_FOUND,
                'message' : "permissions not found",
                'body' : []
            }
        data = add_permission(
            target='groups',
            target_id=update_data.get('id'),
            data={'permissions' : api_objects.get('body')}
        )
        if not data.get('body'):
            response.status_code = status.HTTP_404_NOT_FOUND
        return data
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='server connection error'
        )


@permissions_management.put('/permissions/group/update')
def update_permissions_in_groups(
    request : Request,
    response : Response,
    update_data : AddPermissionsInGroupModal
    ):
    """
    This api adds the extra permissions in group
    - Body : 
        - update_data : contain group id and list for permissions id
    """
    try:
        update_data = update_data.dict(exclude_unset=True)
        api_permissions_ids = update_data.get('api_permissions')
        if not api_permissions_ids:
            response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
            return {
                'status' : 422,
                'message' : "permissions object not provided"
            }
        api_objects = DBQuery().find(
                collection=GROUPS_TABLE.get('apis'),
                query={"id" : {"$in" : api_permissions_ids}}
            )
        if not  api_objects.get('body'):
            response.status_code = status.HTTP_404_NOT_FOUND
            return {
                'status' : status.HTTP_404_NOT_FOUND,
                'body' : []
            }
        data = update_permission(
            target=GROUPS_TABLE.get('groups'),
            target_id=update_data.get('id'),
            data=api_objects.get('body')
        )
        return data
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='server connection error'
        )

@permissions_management.put('/permissions/group/remove')
def remove_permissions_in_groups(
    request : Request,
    response : Response,
    update_data : AddPermissionsInGroupModal
    ):
    """
    This api removes some permissions from group
    - Body : 
        - update_data : contain group id and list of permissions id
        which we want to remove
    """
    try:
        update_data = update_data.dict(exclude_unset=True)
        api_permissions_ids = update_data.get('api_permissions')
        if not api_permissions_ids:
            response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
            return {
                'status' : 422,
                'message' : "permissions object not provided"
            }
        api_objects = DBQuery().find(
                collection=GROUPS_TABLE.get('apis'),
                query={"id" : {"$in" : api_permissions_ids}}
            )
        if not  api_objects.get('body'):
            response.status_code = status.HTTP_404_NOT_FOUND
            return {
                'status' : status.HTTP_404_NOT_FOUND,
                'body' : []
            }
        data = update_permission(
            target=GROUPS_TABLE.get('groups'),
            target_id=update_data.get('id'),
            data=api_objects.get('body'),
            remove = True
        )
        return data
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='server connection error'
        )




