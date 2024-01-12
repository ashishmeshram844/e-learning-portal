
from bson.json_util import dumps
import json
from fastapi import status
import inspect
from config.logger.all_loggers import create_db_log_message



def generate_response(data):
    if isinstance(data,list) or isinstance(data,dict):
        return {
            'status' : status.HTTP_200_OK,
            'body' : data
        }
    else:
        create_db_log_message(
            message=f"response data is not in list or dictionary format",
            state=('info'),
            module=f"{__name__}.{inspect.stack()[0][3]}"
        )
    return None

def convert_json(cursor = None):
    try:
        cursor = dumps(cursor)
        return json.loads(cursor)
    except Exception as e:
        create_db_log_message(
            message=f"failed to convert data into json",
            state=('info'),
            module=f"{__name__}.{inspect.stack()[0][3]}"
        )
        return None
