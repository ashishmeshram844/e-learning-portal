from fastapi import APIRouter,Request, Response,status
from .modal import CreatePermissionModel,PermissionsListModel,UpdatePermissionModel
from dbs.mongo.queries.user_query import DBQuery
from .tables import PERMISSION_TABLE
from fastapi.exceptions import HTTPException

permissions_management = APIRouter(
    prefix= '/permissions',
    tags= ["Permissions Management"]
)

@permissions_management.post(
    path='/',
    summary="Create New Permission"
    )
def create_permission(
    request : Request,
    response : Response,
    create_data : CreatePermissionModel
    ):
    try:
        data = DBQuery().create(
            collection=PERMISSION_TABLE.get('permissions',None),
            data=create_data.dict()
        )
        print(data)
        response.status_code = status.HTTP_201_CREATED
        return create_data.dict()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='server connection error'
        ) 
    
@permissions_management.get(
        path='/',
        response_model=PermissionsListModel,
        summary="Get All Permissions List"
    )
def permission_list(
    request : Request,
    response : Response
    ):
    try:
        data = DBQuery().find(
            collection=PERMISSION_TABLE.get('permissions',None),
        )
        return data
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='server connection error'
        )
 
@permissions_management.get(
        path='/{id}',
        summary="Get Permission Detail"
    )
def permission_detail(
    request : Request,
    response : Response,
    id : str 
    ):
    try:
        data = DBQuery().find(
            collection=PERMISSION_TABLE.get('permissions',None),
            query= {'id' : id},
            only_one=True
        )
        if not data.get('body'):
            response.status_code = status.HTTP_404_NOT_FOUND
            return {
                'status' :404,
                'body' : []
            }
        return data
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='server connection error'
        )
    
@permissions_management.delete(
        path='/{id}',
        summary="Delete Permission"
    )
def delete_permission(
    request:Request,
    response:Response,
    id : str
):
    try:
        data = DBQuery().delete(
                collection=PERMISSION_TABLE.get('permissions',None),
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

@permissions_management.put(
        path='/{id}',
        summary= "Update Permission Details"
    )
def update_permission(
    request:Request,
    response : Response,
    id : str,
    update_data : UpdatePermissionModel
    )  :
  
    try:
        # for partial update
        update_data = update_data.dict(exclude_unset=True)
        data = DBQuery().update(
            collection=PERMISSION_TABLE.get('permissions',None),
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
        pass
    response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    raise HTTPException(
        status_code=500,
        detail='server connection error'
    )

