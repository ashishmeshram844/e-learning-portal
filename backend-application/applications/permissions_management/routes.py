from fastapi import APIRouter,Request, Response,status
from dbs.mongo.queries.user_query import DBQuery
from fastapi.exceptions import HTTPException
from applications.groups_management.tables import GROUPS_TABLE
from .modals import AddPermissionsInGroupModal

permissions_management = APIRouter(
    prefix= '/permission',
    tags= ["Permission Management"]
)


def add_permission(
    target : str = None,
    target_id : str = None,
    data : dict = {}
    ):
    try:
        if not target:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail='server connection error'
            )
        # update  permissions 
        response_data = DBQuery().update(
            collection=target,
            query={'id' : target_id},
            update_data=data
        )
        if response_data.get('status') == 200 and response_data.get('body'):
            return DBQuery().find(
                collection=target,
                query={'id' : target_id},
                only_one=True
            )
        return {
            'status' : status.HTTP_404_NOT_FOUND,
            'body' : []
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='server connection error'
        )

def update_permission(
    target : str = None,
    target_id : str = None,
    data : dict = {},
    remove = None
    ):
    try:
        if not target:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail='server connection error'
            )
        # update  permissions 
        target_object = DBQuery().find(
            collection=target,
            query={'id' : target_id},
            only_one=True
        )    
        if not target_object.get('body'):
            return {
                'status' : 404,
                'body' : []
            }
        old_permissions = target_object.get('body')[0].get('permissions',None)
        try:
            old_permissions_endpoints = [i.get('path',None)   for i in old_permissions]
        except Exception as e:
            print(e)
        set_to_data =list()
        for counter,parsed_per in enumerate(data):
            if not remove:
                if parsed_per.get('path') not in old_permissions_endpoints:
                    set_to_data.append(parsed_per)
            else:
                if parsed_per.get('path')  in old_permissions_endpoints:
                    set_to_data.append(parsed_per.get('path',None))
        if not set_to_data:
            return {
                'status' : 422,
                'message' : 'no new permission provided'
            }
        res = DBQuery().update_set_to(
            collection= target,
            query={"id" : target_id},
            update_data=set_to_data,
            remove = remove
            )
        target_object = DBQuery().find(
            collection=target,
            query={'id' : target_id},
            only_one=True
        )
        return target_object
    except Exception as e:
        # print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='server connection error'
        )


@permissions_management.post(
        path='/permissions/add',
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


@permissions_management.put('/permissions/update')
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

@permissions_management.put('/permissions/remove')
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




