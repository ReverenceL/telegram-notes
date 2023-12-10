from aiogram_dialog import Dialog, Window, LaunchMode
from aiogram_dialog.widgets.kbd import Start, Row, Button
from aiogram_dialog.widgets.text import Const

from bot.dialogs.states import MainSG, NotesListSG
from .handlers import create_note

main_menu_dialog = Dialog(
    Window(
        Const("📝 Заметки "),
        Row(
            Start(Const("🧾 Список"), id="open.notes.list", state=NotesListSG.MENU),
            Button(Const("✍️ Создать"), id="open.empty.note", on_click=create_note),
        ),
        state=MainSG.MENU,
    ),
    launch_mode=LaunchMode.ROOT,
)
