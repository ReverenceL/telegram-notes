from aiogram import Dispatcher
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from bot.middlewares.repo import RepoMiddleware


def setup_middlewares(dp: Dispatcher, db_pool: async_sessionmaker[AsyncSession]):
    dp.update.middleware(RepoMiddleware(db_pool))
