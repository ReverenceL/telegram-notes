from aiogram.fsm.state import StatesGroup, State


class MainSG(StatesGroup):
    MENU = State()


class NotesListSG(StatesGroup):
    MENU = State()


class NoteSG(StatesGroup):
    MENU = State()
    UPDATE_TITLE = State()
    UPDATE_TEXT = State()


class SearchNotesSG(StatesGroup):
    GET_NOTE_NAME = State()
