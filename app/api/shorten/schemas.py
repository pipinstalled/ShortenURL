from datetime import datetime
from pydantic import BaseModel


class UrlCreate(BaseModel):
    original_url: str


class UrlResponse(BaseModel):
    id: int
    original_url: str
    short_code: str
    created_at: datetime
    message: str