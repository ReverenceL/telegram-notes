from aiogram.types import User
from aiogram_dialog import DialogManager

from bot.db.repositories import Repo
from bot.dialogs.states import NoteSG


async def create_note(_, __, manager: DialogManager):
    repo: Repo = manager.middleware_data["repo"]
    user: User = manager.middleware_data["event_from_user"]
    note_id = await repo.note.create(user.id, "Без названия", "Текст заметки, максимальное количество символов - 3000")
    await repo.commit()
    await manager.start(NoteSG.MENU, data={"note_id": note_id})
