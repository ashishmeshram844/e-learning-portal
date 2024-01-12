from dbs.mongo.get_db import get_db
from dbs.db_names import ALL_DATABASES
from bson.json_util import dumps
import json
from fastapi.exceptions import HTTPException

DB = ALL_DATABASES.get('users_db')

def find(collection : str = None, 
         query: dict = {}):
    if collection:
        cursor = get_db(DB)[collection].find(query,{"_id":0})
        cursor = dumps(cursor)
        return json.loads(cursor)
    else:
        raise HTTPException(status_code=500,detail="server connection error")