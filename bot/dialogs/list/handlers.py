from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager

from bot.db.repositories import Repo
from bot.dialogs.states import NoteSG


async def select_note(callback_query: CallbackQuery, _, manager: DialogManager, note_id: int):
    repo: Repo = manager.middleware_data["repo"]
    note = await repo.note.get_by_id(note_id)
    if note is None:
        await callback_query.answer("Заметка не найдена")
        return
    await manager.start(NoteSG.MENU, data={"note_id": note_id})
