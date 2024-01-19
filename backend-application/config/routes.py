from routes.users.user import user
from config.settings.base_settings import app
from fastapi import APIRouter

from applications.authentication.routes import auth
app.include_router(user)
app.include_router(auth)