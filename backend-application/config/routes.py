from . import *


app.include_router(apis_management)
app.include_router(authentication)
app.include_router(roles_management)
app.include_router(group_management)
app.include_router(user_management)
app.include_router(permissions_management)
