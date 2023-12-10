from typing import Any

from aiogram.types import User
from aiogram_dialog import DialogManager

from bot.db.models import Note
from bot.db.repositories import Repo


async def get_user_notes(
        repo: Repo,
        event_from_user: User,
        dialog_manager: DialogManager,
        **_: Any,
) -> dict[str, list[Note]]:
    title_for_search = dialog_manager.dialog_data.get("title_for_search")
    if title_for_search:
        notes = await repo.note.search_by_title(event_from_user.id, title_for_search)
    else:
        notes = await repo.note.get_by_user_id(event_from_user.id)
    return {
        "notes": notes,
    }
