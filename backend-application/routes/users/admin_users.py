from fastapi import APIRouter,Request

admin_user = APIRouter(
    prefix= '/admin',
    tags= ["ADMIN USER"]
)


@admin_user.get('/')
def admin_user_root(request:Request):
    return {
        'admin' : 'admin user root success'
    }