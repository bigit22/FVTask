from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from src.core.config import settings


engine = create_async_engine(settings.DATABASE_URL)
session = async_sessionmaker(engine, expire_on_commit=False)


async def get_session() -> AsyncSession:
    async with session() as se:
        yield session
