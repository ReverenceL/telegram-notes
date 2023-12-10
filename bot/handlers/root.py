from aiogram import Router
from aiogram.filters import CommandStart
from aiogram_dialog import DialogManager

from bot.dialogs.states import MainSG

router = Router()


@router.message(CommandStart())
async def process_start(_, dialog_manager: DialogManager):
    await dialog_manager.start(MainSG.MENU)
