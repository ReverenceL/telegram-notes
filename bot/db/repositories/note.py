from typing import Sequence

from sqlalchemy import update, delete, select

from bot.db.models.note import Note
from bot.db.repositories.base import BaseRepo


class NoteRepo(BaseRepo):
    async def create(self, user_id: int, title: str, text: str) -> int:
        note = Note()
        note.user_id = user_id
        note.title = title
        note.text = text
        self.session.add(note)
        await self.session.flush()
        return note.id

    async def get_by_id(self, note_id: int) -> Note | None:
        return await self.session.get(Note, note_id)

    async def get_by_user_id(self, user_id: int) -> Sequence[Note]:
        result = await self.session.scalars(
            select(Note)
            .where(Note.user_id == user_id)
        )
        return result.all()

    async def search_by_title(self, user_id: int, title: str) -> Sequence[Note]:
        result = await self.session.scalars(
            select(Note)
            .where(Note.user_id == user_id, Note.title.like(f"%{title}%"))
        )
        return result.all()

    async def update_title(self, note_id: int, title: str) -> None:
        await self.session.execute(
            update(Note)
            .where(Note.id == note_id)
            .values(title=title)
        )

    async def update_text(self, note_id: int, text: str) -> None:
        await self.session.execute(
            update(Note)
            .where(Note.id == note_id)
            .values(text=text)
        )

    async def delete(self, note_id: int) -> None:
        await self.session.execute(
            delete(Note)
            .where(Note.id == note_id)
        )
