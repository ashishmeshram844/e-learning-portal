from fastapi import APIRouter,Request
from routes.users.routes import user
from dbs.mongo.queries.user_query import find
import json
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse
from config.logger.all_loggers import create_user_log_message

@user.get('/')
async def get_users(request:Request):
    try:
        data = find(collection='users',query={'username':"ashish"})
        return JSONResponse(data)
    except Exception as e:
        create_user_log_message(
            message=f'failed to get users list because : {e}',
            state="error",
            module = __name__
        )
        print(e)
        raise HTTPException(status_code=500,detail='server connection error')

@user.post('/')
def create_user(request:Request):
    pass

