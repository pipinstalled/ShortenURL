from functools import wraps
from fastapi import Request
from sqlalchemy.orm import Session
from core.database import Url, UrlVisit


def log_visit(func):
    @wraps(func)
    async def wrapper(short_code: str, request: Request, db: Session):

        response = await func(short_code, request, db)

        if response.status_code == 302:
            ip = request.client.host if request.client else "Unknown"

            url_record = db.query(Url).filter(Url.short_code == short_code).first()
            if url_record:
                visit = UrlVisit(url_id=url_record.id, ip_address=ip)
                db.add(visit)
                db.commit()

        return response

    return wrapper