"""
all dependencies related to permissions
- has permission in group
- has permission in role
- has permission in logged in user or tokened user
- check permission available in group or role or user
"""



from applications.authentication.routes import get_token_user
from fastapi import Depends,status
from fastapi.exceptions import HTTPException

async def check_permission_in_group(
    endpoint_url = None,
    tokened_user  = Depends(get_token_user)
    ):
    try:
        # print(tokened_user)
        return tokened_user
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="server connection error"
        )


