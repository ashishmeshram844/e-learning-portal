from config.settings.base_settings import app
from applications.user_management.routes import user_management
from applications.authentication.routes import authentication

app.include_router(authentication)
app.include_router(user_management)