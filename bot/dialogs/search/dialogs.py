from aiogram_dialog import Window, Dialog
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.text import Const

from bot.dialogs.search.handlers import get_title_for_search
from bot.dialogs.states import SearchNotesSG

search_note_dialog = Dialog(
    Window(
        Const("🔍 Отправьте название заметки:"),
        TextInput(
            id="get.note.title",
            on_success=get_title_for_search,
        ),
        state=SearchNotesSG.GET_NOTE_NAME,
    ),
)
