from sqlalchemy import make_url
from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker, AsyncSession, create_async_engine

from bot.config import DBConfig


def create_pool(config: DBConfig) -> async_sessionmaker[AsyncSession]:
    engine = create_engine(config)
    return create_session_maker(engine)


def create_engine(config: DBConfig) -> AsyncEngine:
    return create_async_engine(url=make_url(config.full_url))


def create_session_maker(engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
    session_maker = async_sessionmaker(
        bind=engine, expire_on_commit=False, autoflush=False,
    )
    return session_maker
