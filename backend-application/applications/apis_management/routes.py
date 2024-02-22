"""
Contain all api routes for api managements
- This module help to define permissions on api level 
- minor level permissions objects on every apis endpoints
- get all apis list
- reset all apis list
"""
from . import (
    ApiMethodsInput, ApiListResponse,
    APIRouter,Request,Response,status,HTTPException,
    ApiMethodsInput, ApiListResponse,
    create_user_log_message,inspect,socket,
    ERR_RESPONSES,get_filtered_apis,override_apis
)

hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)

API_PROJECT_IP = "127.0.0.1:5000"

apis_management = APIRouter(
    prefix= '/apis',
    tags= ["Apis Management"],
)

@apis_management.get(
        path='/',
        summary='Apis list',    
        response_model= ApiListResponse
    )
def get_apis_list(
    request : Request,
    response : Response,
    body_data : ApiMethodsInput,
    ):
    """
    ### This api gives all available apis list
    - Client can access this endpoints response if they have\n
    permissions then only they can access else unauthorized reponse 
    #### Body :
    - methods : (array) 
    """
    try:
        body_methods = body_data.methods
        if not body_methods:
            response.status_code = status.HTTP_404_NOT_FOUND
            return ERR_RESPONSES[404]
        apis_list = get_filtered_apis(mthd=body_methods)
        return {
            'status' : status.HTTP_200_OK,
            'body' : apis_list
        }
    except Exception as e:
        create_user_log_message(
            message=f'failed to get apis list because : {e}',
            state="error",
            module=f"{__name__}.{inspect.stack()[0][3]}"
        )
    raise HTTPException(
        status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail = "server connection error"
    )

@apis_management.head(
        path='/reset_all_api',
        summary='Reset all api endpoints in db',    
        include_in_schema=False
    )
def reset_all_apis_in_db(
    request : Request,
    response : Response,
    ):
    """
    This api reset all api objects in apis collections
    - this delete all previous objects and add new objects again 
    - note :  ids of this objects will be chnaged everytime \n
    whenever we reset
    """
    try:
        result = override_apis(all_routes = request.app.routes)
        if result:
            response.status_code = status.HTTP_205_RESET_CONTENT
        return {}
    except Exception as e:
        create_user_log_message(
            message=f'failed to reset api list because : {e}',
            state="error",
            module=f"{__name__}.{inspect.stack()[0][3]}"
        )
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail='server connection error'
    )

