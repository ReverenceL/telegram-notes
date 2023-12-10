from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager

from bot.db.repositories import Repo
from bot.dialogs.states import NotesListSG, NoteSG


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


async def update_note_title(_, __, manager: DialogManager, title: str):
    repo: Repo = manager.middleware_data["repo"]
    await repo.note.update_title(manager.dialog_data["note_id"], title)
    await repo.commit()
    await manager.switch_to(NoteSG.MENU)


async def update_note_text(_, __, manager: DialogManager, text: str):
    repo: Repo = manager.middleware_data["repo"]
    await repo.note.update_text(manager.dialog_data["note_id"], text)
    await repo.commit()
    await manager.switch_to(NoteSG.MENU)


async def too_long_title(message: Message, _, __, ___):
    await message.answer("Вы ввели слишком длинное название.")


async def too_long_text(message: Message, _, __, ___):
    await message.answer("Вы ввели слишком длинный текст заметки.")
