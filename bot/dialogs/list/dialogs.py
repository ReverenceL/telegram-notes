from aiogram import F
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import ScrollingGroup, NextPage, PrevPage, Row, Select, Start, CurrentPage
from aiogram_dialog.widgets.text import Const, Format

from bot.dialogs.list.getters import get_user_notes
from bot.dialogs.list.handlers import select_note
from bot.dialogs.states import NotesListSG, MainSG

notes_list_dialog = Dialog(
    Window(
        Const("📋 Список ваших заметок:"),
        ScrollingGroup(
            Select(
                Format("{item.title}"),
                id="select",
                item_id_getter=lambda note: note.id,
                items="notes",
                type_factory=int,
                on_click=select_note,
            ),
            id="paginator",
            width=1,
            height=10,
            hide_pager=True,
        ),
        Row(
            PrevPage(
                scroll="paginator",
                text=Format("◀️"),
                when=F["pages"] != 0,
            ),
            CurrentPage(
                scroll="paginator",
                text=Format("{current_page1}/{pages}"),
                when=F["pages"] != 0,
            ),
            NextPage(
                scroll="paginator",
                text=Const("▶️"),
                when=F["pages"] != 0,
            ),
        ),
        Start(Const("Назад"), id="close.list", state=MainSG.MENU),
        state=NotesListSG.MENU,
        getter=get_user_notes,
    ),
)
