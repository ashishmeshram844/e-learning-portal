from dbs.mongo.queries.user_query import DBQuery
from fastapi.exceptions import HTTPException
from dbs.mongo.get_db import get_db
from .tables import APIS_TABLES
from dbs.db_names import ALL_DATABASES


def get_all_apis_list():
    """
    This functin fetch all apis list from collection 
    """
    try:
        all_db_apis =  DBQuery().find(
                collection='apis'
            )
        return all_db_apis  
    except Exception as e:
        raise HTTPException(
            status_code = 500,
            detail = "Server connection error"
        )
    
def drop_api_collection():
    try:
        get_db(
            db_name=ALL_DATABASES.get('users_db',None)
            )[APIS_TABLES.get('apis')].drop()
        return True
    except Exception as e:
        return False

def add_apis_in_db(apis : list = []):
    if not apis:
        return None
    try:
        get_db(
            db_name=ALL_DATABASES.get('users_db',None)
            )[APIS_TABLES.get('apis')].insert_many(
                apis
            )
        return True
    except Exception as e:
        return 
