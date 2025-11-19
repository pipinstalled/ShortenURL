from fastapi import FastAPI
from core.database import get_db
from core.config import settings


app = FastAPI( title=settings.APP_NAME)
