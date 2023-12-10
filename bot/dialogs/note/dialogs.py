from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Start, Button, Row
from aiogram_dialog.widgets.text import Multi, Jinja, Const

from bot.dialogs.note.getters import get_note_data
from bot.dialogs.note.handlers import delete_note
from bot.dialogs.states import NoteSG, NotesListSG
from bot.utils import transfer_start_data

note_dialog = Dialog(
    Window(
        Multi(
            Jinja("📝 Заметка: {{ title }}"),
            Jinja("{{ text }}"),
            sep="\n\n",
        ),
        Row(
            Start(Const("◀️ Назад"), id="close.note", state=NotesListSG.MENU),
            Button(Const("🗑 Удалить"), id="delete.note", on_click=delete_note),
        ),
        state=NoteSG.MENU,
        getter=get_note_data,
    ),
    on_start=transfer_start_data,
)
