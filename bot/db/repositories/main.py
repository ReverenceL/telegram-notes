from sqlalchemy.ext.asyncio import AsyncSession

from bot.db.repositories.base import BaseRepo


class Repo(BaseRepo):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)
