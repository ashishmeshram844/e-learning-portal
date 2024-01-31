from fastapi import APIRouter,Request,Response,status
from .modals import RolesInput, RolesListModel,UpdateRoleModel,AssignRoleToUserRequestModal
from dbs.mongo.queries.user_query import DBQuery
from .tables import ROLE_TABLES
from fastapi.exceptions import HTTPException

roles_management = APIRouter(
    prefix= '/roles',
    tags= ["Roles Management"]
)

@roles_management.post(
        path='/',
        response_model=RolesInput,
        summary="Create New Role"    
    )
def create_role(
    request : Request,
    response : Response,
    create_data : RolesInput
    ):
    """
    Create a new role 
    """
    try:
        data = DBQuery().create(
            collection=ROLE_TABLES.get('roles',None),
            data=create_data.dict()
        )
        response.status_code = status.HTTP_201_CREATED
        return create_data.dict()
    except Exception as e:
        raise HTTPException(
            status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='server connection error'
        )

@roles_management.get(
        path='/',
        response_model=RolesListModel,
        summary="Get All Roles List"
    )
def roles_list(
    request : Request,
    response : Response
    ):
    """
    Ferch all roles list which are available in collection or db
    """
    try:
        data = DBQuery().find(
            collection=ROLE_TABLES.get('roles',None),
        )
        return data
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='server connection error'
        )
    
@roles_management.get(
        path='/{id}',
        summary="Get Role Detail"
    )
def role_detail(
    request : Request,
    response : Response,
    id : str 
    ):
    """
    Fetnch detail of specific role
    """
    try:
        data = DBQuery().find(
            collection=ROLE_TABLES.get('roles',None),
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
    
@roles_management.delete(
        path='/{id}',
        summary="Delete Role"
    )
def delete_role(
    request:Request,
    response:Response,
    id : str
    ):
    """
    This deletes a specific role which client provide
    """
    try:
        data = DBQuery().delete(
                collection=ROLE_TABLES.get('roles',None),
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



@roles_management.put(
        path='/{id}',
        summary= "Update Role Details"
    )
def update_role(
    request:Request,
    response : Response,
    id : str,
    update_data : UpdateRoleModel
    ):
    """
    Updates the role detail 
    """
    try:
        # for partial update
        update_data = update_data.dict(exclude_unset=True)
        data = DBQuery().update(
            collection=ROLE_TABLES.get('roles',None),
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


from applications.user_management.routes import update_user,get_user_detail
from applications.user_management.modals import UpdateUserModel

@roles_management.post(
    path='/assign/user',
    summary="Assign role to User"
)
def assign_user_role(
    request : Request,
    response : Response,
    data : AssignRoleToUserRequestModal
    ):
    result = update_user(
        request=request,
        response=response,
        id=data.user_id,
        update_data=UpdateUserModel(role = data.user_id)
    )
    print("UPDATES : ",result)
    return result

