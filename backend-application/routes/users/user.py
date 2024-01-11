from fastapi import APIRouter,Request

user = APIRouter(
    prefix= '/users',
    tags= ["ADMIN USER"]
)


@user.get('/')
def get_users(request:Request):
    return {
        'admin' : 'all users list'
    }


