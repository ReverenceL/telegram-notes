from aiogram_dialog import DialogManager

from bot.dialogs.states import NotesListSG


async def get_title_for_search(_, __, manager: DialogManager, title: str):
    await manager.start(
        NotesListSG.MENU,
        data={"title_for_search": title},
    )
