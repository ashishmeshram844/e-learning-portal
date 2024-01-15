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

def GET_DB_OBJ(db = DB):
    try:
        return get_db(db_name=db)
    except Exception as e:
        create_db_log_message(
            message=f"Failed to connect {db} database",
            state=('info'),
            module=f"{__name__}.{inspect.stack()[0][3]}"
        )
    raise HTTPException(
        status_code=500,
        detail="DB connection error"
        )


class DBQuery():
    def __init__(self):
        self.DB_OBJ = GET_DB_OBJ(db = DB)

    def find(
            self,
            collection : str = None, 
            query: dict = {}
            ):
        try:
            if collection:
                cursor = self.DB_OBJ[collection].find(
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
            self,
            collection = None,
            data : dict | list = None
            ):
        try:
            if collection:
                if data:
                    cursor = self.DB_OBJ[collection].insert_one(
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
            update_query = { 
                "$set": update_data
            }
            self.DB_OBJ[collection].update_one(
                query,
                update_query
            )
            updated_data = self.find(
                collection=collection,
                query=query
            )
            return updated_data
        except Exception as e:
            create_db_log_message(
                message=f"Error Occured while executing Update query on {DB} database and {collection} collection because : {e}",
                state=('error'),
                module=f"{__name__}.{inspect.stack()[0][3]}"
            )
        raise HTTPException(
            status_code=500,
            detail="server connection error"
            )   