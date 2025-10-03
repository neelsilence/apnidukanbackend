from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .base import Base
from app.core.config import settings

# check_same_thread is needed for SQLite in multithreaded FastAPI dev server
engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URI,
    connect_args={"check_same_thread": False} if settings.SQLALCHEMY_DATABASE_URI.startswith("sqlite") else {}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    # Import models so tables are registered with Base.metadata
    from app.models import product  # noqa: F401
    Base.metadata.create_all(bind=engine)
