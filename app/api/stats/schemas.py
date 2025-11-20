from datetime import datetime
from pydantic import BaseModel


class UrlStatsResponse(BaseModel):
    original_url: str
    short_code: str
    created_at: datetime
    visits_count: int