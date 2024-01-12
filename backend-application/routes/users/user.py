from fastapi import APIRouter,Request
from routes.users.routes import user
from dbs.mongo.queries.user_query import find
import json


@user.get('/')
def get_users(request:Request):
    data = find(collection='users',query={'name':"Ashish"})
    print(data)
    return {
        'data' : data
    }


