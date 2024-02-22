from applications.user_management.validators import *
from .db_operations import (
    get_all_apis_list,drop_api_collection,
    add_apis_in_db
)
from fastapi.exceptions import HTTPException
import uuid

API_PROJECT_IP = "127.0.0.1:5000"

def get_filtered_apis(
        mthd : list = [],
    ) -> list:
    """
    This function filters the api as per parsed methods list
    """
    all_db_apis = get_all_apis_list()
    try:
        apis_list = [
            {
                'id': route['id'],
                'path': route['path'],
                'name': route['name'],
                'summary': route['summary'],
                'method': route['method']
            }
            for route in all_db_apis.get('body', [])
            if any(req_mtd.upper() in route['method'] for req_mtd in mthd)
        ]
        return apis_list
    except Exception as e:
        raise HTTPException(
            status_code = 500,
            detail = "Server connection error"
        )

def override_apis(all_routes = None):
    """
    This function override all apis list in db collection
    """
    try:
        if not all_routes:
            return None
        apis_list = list()
        for route in all_routes:
            api_summary = None
            try:api_summary = route.summary
            except:...
            apis_list.append( 
                {   'id' : str(uuid.uuid4()),
                    'path': f'http://{API_PROJECT_IP}{route.path}', 
                    'name': route.name,
                    'summary' : api_summary,
                    'method' : list(route.methods)
                }
            )
        drop_api_collection()
        add_apis_in_db(apis=apis_list)
        return True
    except Exception as e:
        raise HTTPException(
            status_code = 500,
            detail = 'server connection error'
        )
