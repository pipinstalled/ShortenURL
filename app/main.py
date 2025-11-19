from fastapi import FastAPI
from core.database import get_db
from core.config import settings
from api.shorten.api import router as shorten_router


app = FastAPI( title=settings.APP_NAME)

app.include_router(shorten_router)