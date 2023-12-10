from aiogram import Dispatcher

from bot.dialogs.list.dialogs import notes_list_dialog
from bot.dialogs.note import note_dialog
from bot.dialogs.root import main_menu_dialog


def setup_dialogs(dp: Dispatcher) -> None:
    dp.include_routers(
        main_menu_dialog,
        notes_list_dialog,
        note_dialog,
    )
