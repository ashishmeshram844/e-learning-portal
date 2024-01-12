from dbs.mongo.get_db import get_db
from dbs.db_names import ALL_DATABASES
from bson.json_util import dumps
import json
from fastapi.exceptions import HTTPException
from fastapi import status

DB = ALL_DATABASES.get('users_db')



def generate_response(data):
    if isinstance(data,list) or isinstance(data,dict):
        return {
            'status' : status.HTTP_200_OK,
            'body' : data
        }
    return None




def convert_json(cursor = None):
    try:
        cursor = dumps(cursor)
        return json.loads(cursor)
    except Exception as e:
        return None
    
def find(collection : str = None, 
         query: dict = {}
         ):
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
        pass
    raise HTTPException(
        status_code=500,
        detail="server connection error"
        )