from dbs.mongo.get_db import get_db
from dbs.db_names import ALL_DATABASES
from bson.json_util import dumps
import json
from fastapi.exceptions import HTTPException
from fastapi import status
import inspect
from config.logger.all_loggers import create_db_log_message
from .commons import convert_json,generate_response

DB = ALL_DATABASES.get('users_db')

    
def find(collection : str = None, 
         query: dict = {}
         ):
    try:
        if collection:
            cursor = get_db(DB)[collection].find(
                query,
                {"_id":0}
                )
            cursor = convert_json(
                cursor=cursor
                )        
            return generate_response(
                data=cursor
                )
        else:
            create_db_log_message(
                    message=f"collection not provided while communicating with {DB} database",
                    state=('info'),
                    module=f"{__name__}.{inspect.stack()[0][3]}"
                )
    except Exception as e:
        create_db_log_message(
            message=f"Error while fetching data from {collection}  table using {DB} database because : {e}",
            state=('info'),
            module=f"{__name__}.{inspect.stack()[0][3]}"
        )
    raise HTTPException(
            status_code=500,
            detail="server connection error"
            )

def create(
        collection = None,
        data : dict | list = None
        ):
    if collection:
        if data:
            cursor = get_db(DB)[collection].insert_one(
                data
                )
            return cursor
        else:
            create_db_log_message(
                message=f"Proper data not provided for adding in collection : {collection} in {DB} database",
                state=('info'),
                module=f"{__name__}.{inspect.stack()[0][3]}"
            )
    else:
        create_db_log_message(
            message=f"collection not provided while communicating with {DB} database",
            state=('info'),
            module=f"{__name__}.{inspect.stack()[0][3]}"
        )
    raise HTTPException(
            status_code=500,
            detail="server connection error"
            )