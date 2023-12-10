from aiogram.fsm.state import StatesGroup, State


class MainSG(StatesGroup):
    MENU = State()


class NotesListSG(StatesGroup):
    MENU = State()


class NoteSG(StatesGroup):
    MENU = State()
