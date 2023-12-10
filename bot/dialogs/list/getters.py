from aiogram.types import User

from bot.db.models import Note
from bot.db.repositories import Repo


async def get_user_notes(repo: Repo, event_from_user: User, **_) -> dict[str, list[Note]]:
    return {
        "notes": await repo.note.get_by_user_id(event_from_user.id),
    }
