from fastapi import FastAPI
from core.database import get_db

app = FastAPI( title="ShortURL API")
