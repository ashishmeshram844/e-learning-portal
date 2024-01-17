from fastapi import APIRouter

user = APIRouter(
    prefix= '/users',
    tags= ["Users"]
)



auth = APIRouter(
    prefix= '/auth',
    tags= ["Authentication"]
)