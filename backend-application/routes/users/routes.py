from fastapi import APIRouter

user = APIRouter(
    prefix= '/users',
    tags= ["Users"]
)
