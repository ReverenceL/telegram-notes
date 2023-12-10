from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager

from bot.db.repositories import Repo
from bot.dialogs.states import NotesListSG


async def delete_note(callback_query: CallbackQuery, _, manager: DialogManager):
    repo: Repo = manager.middleware_data["repo"]
    attempts = manager.dialog_data.get("attempts", 0)
    if attempts == 0:
        await callback_query.answer("Подтвердите удаление заметки еще одним нажатием.")
        manager.dialog_data["attempts"] = 1
        return

    await repo.note.delete(manager.dialog_data["note_id"])
    await repo.commit()
    await manager.start(NotesListSG.MENU)
