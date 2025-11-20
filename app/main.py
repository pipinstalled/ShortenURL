from fastapi import FastAPI
from core.database import get_db
from core.config import settings
from api.shorten.api import router as shorten_router
from api.redirect.api import router as redirect_router
from api.stats.api import router as stats_router

app = FastAPI( title=settings.APP_NAME)

app.include_router(shorten_router)
app.include_router(redirect_router)
app.include_router(stats_router)