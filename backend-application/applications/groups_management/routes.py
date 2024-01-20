from fastapi import APIRouter,Request, Response,status
from .modal import CreateGroupsModel,GroupsListModel,UpdateGroupsModel
from dbs.mongo.queries.user_query import DBQuery
from .tables import GROUPS_TABLE
from fastapi.exceptions import HTTPException

group_management = APIRouter(
    prefix= '/groups',
    tags= ["Groups Management"]
)

@group_management.post(
    path='/',
    summary="Create New Group"
    )
def create_group(
    request : Request,
    response : Response,
    create_data : CreateGroupsModel
    ):
    try:
        data = DBQuery().create(
            collection=GROUPS_TABLE.get('groups',None),
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
    
@group_management.get(
        path='/',
        response_model=GroupsListModel,
        summary="Get All groups List"
    )
def groups_list(
    request : Request,
    response : Response
    ):
    try:
        data = DBQuery().find(
            collection=GROUPS_TABLE.get('groups',None),
        )
        return data
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='server connection error'
        )
 
@group_management.get(
        path='/{id}',
        summary="Get Group Detail"
    )
def group_detail(
    request : Request,
    response : Response,
    id : str 
    ):
    try:
        data = DBQuery().find(
            collection=GROUPS_TABLE.get('groups',None),
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
    
@group_management.delete(
        path='/{id}',
        summary="Delete Group"
    )
def delete_group(
    request:Request,
    response:Response,
    id : str
):
    try:
        data = DBQuery().delete(
                collection=GROUPS_TABLE.get('groups',None),
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

@group_management.put(
        path='/{id}',
        summary= "Update group Details"
    )
def update_group(
    request:Request,
    response : Response,
    id : str,
    update_data : UpdateGroupsModel
    ):
  
    try:
        # for partial update
        update_data = update_data.dict(exclude_unset=True)
        data = DBQuery().update(
            collection=GROUPS_TABLE.get('groups',None),
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


