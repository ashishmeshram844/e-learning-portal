from dbs.mongo.get_db import get_db
from dbs.db_names import ALL_DATABASES
from bson.json_util import dumps
import json
from fastapi.exceptions import HTTPException
from fastapi import status
import inspect
from config.logger.all_loggers import create_db_log_message
from .commons import convert_json,generate_response
from dbs.mongo.queries.commons import format_message
from commons.responses import ERR_RESPONSES

DB = ALL_DATABASES.get('users_db')

def GET_DB_OBJ(db = DB):
    try:
        return get_db(db_name=db)
    except Exception as e:
        create_db_log_message(
            message=f"Failed to connect {db} database",
            state=('info'),
            module=f"{__name__}.{inspect.stack()[0][3]}"
        )
    return ERR_RESPONSES.get(503,500)

class DBQuery():
    def __init__(self):
        self.DB_OBJ = GET_DB_OBJ(db = DB)
      
    def find(
            self,
            collection : str = None, 
            query: dict = {},
            only_one = False
            ):
        try:
            if not collection:
                create_db_log_message(
                        message=f"collection not provided",
                        state=('info'),
                        module=f"{__name__}.{inspect.stack()[0][3]}"
                )
                raise HTTPException(
                    status_code=500,
                    detail='server connection error'
                )
            if not only_one:
                cursor = self.DB_OBJ[collection].find(
                    query,
                    {"_id":0}
                )
            else:
                cursor = self.DB_OBJ[collection].find_one(
                    query,
                    {"_id":0}
                )   
            cursor = convert_json(
                cursor=cursor
                )  
            return generate_response(
                data=cursor
                )
        except Exception as e:
            create_db_log_message(
                message=format_message(
                    f"""Error while fetching data from 
                        {DB}.{collection} Because : {e}"""),
                state=('info'),
                module=f"{__name__}.{inspect.stack()[0][3]}"
            )
        raise HTTPException(
            status_code=500,
            detail="server connection error"
        )

    def create(
            self,
            collection = None,
            data : dict | list = None
            ):
        try:
            if not collection:
                create_db_log_message(
                    message=format_message(
                        f"""collection not provided while 
                            communicating with {DB} database"""),
                    state=('info'),
                    module=f"{__name__}.{inspect.stack()[0][3]}"
                )
                return ERR_RESPONSES.get(500,500)
            if data:
                cursor = self.DB_OBJ[collection].insert_one(
                    data
                    )
                return cursor
            else:
                create_db_log_message(
                    message= format_message(
                        f"""Proper data not provided in
                            {DB}.{collection} collection"""),
                    state=('info'),
                    module=f"{__name__}.{inspect.stack()[0][3]}"
                )
        except Exception as e:
            create_db_log_message(
                message=f"Exception occured Because : {e}",
                state=('info'),
                module=f"{__name__}.{inspect.stack()[0][3]}"
            )
        raise HTTPException(
            status_code=500,
            detail="server connection error"
        )

    def update(
            self,
            collection : str | None = None,
            query : dict = {},
            update_data : dict  = {}
        ):
        """
        This function update the data from provided collection and qeury
        """
        try:
            cursor = self.DB_OBJ[collection].find(
                query,
                {"_id":0}
                )
            cursor = convert_json(
                cursor=cursor
                )        
            if cursor:
                update_query = { 
                    "$set": update_data
                }
                self.DB_OBJ[collection].update_one(
                    query,
                    update_query
                )
                updated_data = self.find(
                    collection=collection,
                    query=query,
                    only_one=True
                )
                return updated_data
            else:
                return generate_response(data=cursor)
        except Exception as e:
            create_db_log_message(
                message=format_message(
                    f"""Error Occured while executing Update 
                        query on {DB} database and {collection} 
                        collection because : {e}"""),
                state=('error'),
                module=f"{__name__}.{inspect.stack()[0][3]}"
            )
        raise HTTPException(
            status_code=500,
            detail="server connection error"
        )
    
    def delete(
            self,
            collection = None,
            query = None
        ):
        """
        This function delete the data from provided collection and qeury
        """
        try:
            if not collection:
                create_db_log_message(
                message=format_message(
                    f"""collection not provided in {DB} database 
                        while querying"""),
                state=('error'),
                module=f"{__name__}.{inspect.stack()[0][3]}"
            )
                return ERR_RESPONSES.get(500,500)
            if not query:
                return ERR_RESPONSES.get(404,500)
            found =  self.find(
                collection=collection,
                query=query,
                only_one=True
            )
            if  not found.get('body'):
                return ERR_RESPONSES.get(404,500)
            cursor = self.DB_OBJ[collection].delete_one(
                query,
            )
            cursor = convert_json(
                cursor=cursor
                )      
            return {
                'status' : 200,
                'message' : 'delete successfully',
                'body': []
            }
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail="server connection error"
            )
