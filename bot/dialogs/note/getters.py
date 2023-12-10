from aiogram_dialog import DialogManager

from bot.db.repositories import Repo


async def get_note_data(repo: Repo, dialog_manager: DialogManager, **_) -> dict[str, str]:
    note = await repo.note.get_by_id(dialog_manager.dialog_data["note_id"])
    return {
        "title": note.title,
        "text": note.text,
    }