from routes.users.user import user
from config.settings.base_settings import app
from fastapi import APIRouter

app.include_router(user)