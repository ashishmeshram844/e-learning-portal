from fastapi import status
from dbs.mongo.queries.user_query import DBQuery
from fastapi.exceptions import HTTPException

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
