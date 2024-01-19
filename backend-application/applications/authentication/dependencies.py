from datetime import datetime
from fastapi import HTTPException, status, Header
from jose import jwt
from pydantic import ValidationError
from typing import Annotated
from dbs.mongo.queries.user_query import DBQuery
from .config.jwt import ALGORITHM,JWT_SECRET_KEY


async def get_current_user(
        token: Annotated[str | None, Header()] = None,
        ):
    try:
        if not token:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Token Required"
            )
        payload = jwt.decode(
            token = token, 
            key= JWT_SECRET_KEY, 
            algorithms=[ALGORITHM]
        )
        token_data = payload
        print(token_data)
        
        if datetime.fromtimestamp(token_data.get('exp')) < datetime.now():
            raise HTTPException(
                status_code = status.HTTP_401_UNAUTHORIZED,
                detail="Token expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except(jwt.JWTError, ValidationError) as e:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalidate token",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user = DBQuery().find(
        collection='users',
        query={
            'username' : token_data.get('sub',None)
            }
        )
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not find user",
        )
    return user

