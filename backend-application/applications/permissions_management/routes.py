from fastapi import APIRouter,Request, Response,status
from dbs.mongo.queries.user_query import DBQuery
from fastapi.exceptions import HTTPException
from applications.groups_management.tables import GROUPS_TABLE


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
        # print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='server connection error'
        )





