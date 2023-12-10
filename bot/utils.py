from aiogram_dialog import DialogManager


async def transfer_start_data(start_data: dict, manager: DialogManager):
    manager.dialog_data.update(start_data)
