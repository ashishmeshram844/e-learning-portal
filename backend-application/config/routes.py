from routes.users.admin_users import admin_user
from .base_settings import app

app.include_router(admin_user)