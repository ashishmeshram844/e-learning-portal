from routes.users.user import user
from config.settings.base_settings import app
from fastapi import APIRouter
from routes.users.auth import auth

app.include_router(user)
app.include_router(auth)