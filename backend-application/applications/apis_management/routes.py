"""
Contain all api routes for api managements
- This module help to define permissions on api level 
- minor level permissions objects on every apis endpoints
- get all apis list
- reset all apis list
"""

from fastapi import APIRouter,Request,Response,status
from .tables import APIS_TABLES
from fastapi.exceptions import HTTPException
from .modals import ApiMethodsInput, ApiListResponse
from dbs.mongo.get_db import get_db
from dbs.db_names import ALL_DATABASES
import uuid
from dbs.mongo.queries.commons import convert_json, generate_response
from dbs.mongo.queries.user_query import DBQuery
from config.logger.all_loggers import create_user_log_message
import inspect


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
    - Client can access this endpoints response if they have permissions\n
    then only they can access else unauthorized reponse 
    #### Body :
    - methods : (array) 
    """
    try:
        body_methods = body_data.methods
        if not body_methods:
            response.status_code = status.HTTP_404_NOT_FOUND
            return {
                'status' : status.HTTP_404_NOT_FOUND,
                'body' : []
            }
        apis_list = list()
        all_db_apis =  DBQuery().find(
            collection='apis'
        )
        apis_list = [
            {
                'id': route['id'],
                'path': route['path'],
                'name': route['name'],
                'summary': route['summary'],
                'method': route['method']
            }
            for route in all_db_apis.get('body', [])
            if any(req_mtd.upper() in route['method'] for req_mtd in body_methods)
        ]
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
    - note :  ids of this objects will be chnaged everytime whenever we reset
    """
    try:
        apis_list = list()
        for route in request.app.routes:
            api_summary = None
            try:api_summary = route.summary
            except:pass
            apis_list.append( 
                {   'id' : str(uuid.uuid4()),
                    'path': f'http://{API_PROJECT_IP}{route.path}', 
                    'name': route.name,
                    'summary' : api_summary,
                    'method' : list(route.methods)
                }
            )
        get_db(
            db_name=ALL_DATABASES.get('users_db',None)
            )[APIS_TABLES.get('apis')].drop()
        get_db(
            db_name=ALL_DATABASES.get('users_db',None)
            )[APIS_TABLES.get('apis')].insert_many(
                apis_list
            )
        response.status_code = status.HTTP_205_RESET_CONTENT
        return {}
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='server connection error'
        )
    


