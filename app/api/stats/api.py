
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.stats.schemas import UrlStatsResponse
from services.url_service import get_url_stats

from core.database import get_db
from core.config import settings
router = APIRouter(prefix="/stats",tags=["Statistics of URL"])


@router.get("/{short_code}", response_model=UrlStatsResponse)
async def url_stats(short_code: str, db: Session = Depends(get_db)):
    url_stats, error = get_url_stats(db, short_code)
    if error:
        raise HTTPException(status_code=404, detail=error)
    return url_stats
