from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Start, Button, Row, SwitchTo
from aiogram_dialog.widgets.text import Multi, Jinja, Const

from bot.dialogs.note.getters import get_note_data
from bot.dialogs.note.handlers import delete_note, update_note_title, update_note_text, too_long_title, too_long_text
from bot.dialogs.states import NoteSG, NotesListSG
from bot.utils import transfer_start_data, get_text_length_filter

note_dialog = Dialog(
    Window(
        Multi(
            Jinja("📝 Заметка: {{ title }}"),
            Jinja("{{ text }}"),
            sep="\n\n",
        ),
        SwitchTo(Const("✍️ Обновить название"), id="update.note.title", state=NoteSG.UPDATE_TITLE),
        SwitchTo(Const("📝 Обновить текст"), id="update.note.text", state=NoteSG.UPDATE_TEXT),
        Row(
            Start(Const("◀️ Назад"), id="close.note", state=NotesListSG.MENU),
            Button(Const("🗑 Удалить"), id="delete.note", on_click=delete_note),
        ),
        state=NoteSG.MENU,
        getter=get_note_data,
    ),
    Window(
        Const("✍️ Отправьте новое название: (Не более 64 символов)"),
        TextInput(
            id="get.new.title",
            on_success=update_note_title,
            type_factory=get_text_length_filter(64),
            on_error=too_long_title,
        ),
        state=NoteSG.UPDATE_TITLE,
    ),
    Window(
        Const("📝 Отправьте новый текст заметки: (Не более 3000 символов)"),
        TextInput(
            id="get.new.text",
            on_success=update_note_text,
            type_factory=get_text_length_filter(3000),
            on_error=too_long_text,
        ),
        state=NoteSG.UPDATE_TEXT,
    ),
    on_start=transfer_start_data,

)
