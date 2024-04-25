from sqlalchemy.ext.asyncio import (create_async_engine, async_sessionmaker)
from core.config import settings_db

SQLALCHEMY_DATABASE_URL = f"{settings_db.DATABASE_URI.unicode_string()}"

engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL, echo=True
)
async_session = async_sessionmaker(engine, expire_on_commit=False)
