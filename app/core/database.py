from sqlalchemy.orm import sessionmaker, DeclarativeBase, relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func, create_engine
from core.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    pool_size=10,
    max_overflow=20,
    pool_recycle=3600,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


class Url(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    original_url = Column(String, nullable=False)
    short_code = Column(String(16), unique=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    visits_count = Column(Integer, default=0)
    
    visits = relationship("UrlVisit", back_populates="url")


class UrlVisit(Base):
    __tablename__ = "url_visits"

    id = Column(Integer, primary_key=True)
    url_id = Column(Integer, ForeignKey("urls.id", ondelete="CASCADE"))
    visited_at = Column(DateTime(timezone=True), server_default=func.now())
    ip_address = Column(String, nullable=True)

    url = relationship("Url", back_populates="visits")
    
    
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
