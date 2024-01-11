from routes.users.user import user
from config.settings.base_settings import app
app.include_router(user)