from sqlalchemy.orm import Session
from core.database import Url
from utils.shortener import generate_short_url


def create_short_url(db: Session, original_url: str):
    existing = db.query(Url).filter(Url.original_url == original_url).first()
    if existing:
        return existing, None

    for _ in range(5):
        short_code = generate_short_url()
        exists = db.query(Url).filter(Url.short_code == short_code).first()
        if not exists:
            break
    else:
        return None, "Could not generate unique short code"

    new_url = Url(
        original_url=original_url,
        short_code=short_code
    )

    try:
        db.add(new_url)
        db.commit()
        db.refresh(new_url)
        return new_url, None

    except Exception as e:
        db.rollback()
        return None, "Database error"
