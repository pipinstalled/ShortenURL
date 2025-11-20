
from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from services.url_service import get_url_by_short_code

from core.database import get_db
from core.config import settings
from utils.log_visit import log_visit
router = APIRouter(tags=["Redirect URL"])


@router.get("/{short_code}")
@log_visit
async def redirect_url(short_code: str,request: Request, db: Session = Depends(get_db)):
    original_url, error = get_url_by_short_code(db, short_code)
    if error:
        raise HTTPException(status_code=404, detail=error)
    return RedirectResponse(status_code=302, url=original_url)
