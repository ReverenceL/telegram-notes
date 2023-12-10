from sqlalchemy.ext.asyncio import AsyncSession

from bot.db.repositories.base import BaseRepo
from bot.db.repositories.note import NoteRepo


class Repo(BaseRepo):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)
        self.note = NoteRepo(session)
