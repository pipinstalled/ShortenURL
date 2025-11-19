
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.shorten.schemas import UrlCreate, UrlResponse
from services.url_service import create_short_url

from core.database import get_db
from core.config import settings

router = APIRouter(prefix="/shorten", tags=["Shorten URL"])


@router.post("", response_model=UrlResponse)
def shorten_url(url: UrlCreate, db: Session = Depends(get_db)):
    result, error = create_short_url(db, url.original_url)

    if error:
        raise HTTPException(status_code=400, detail=error)

    return UrlResponse(
        id=result.id,
        original_url=result.original_url,
        short_code=f"{settings.BASE_URL}/{result.short_code}",
        created_at=result.created_at,
        message="Short url created successfully"
    )
