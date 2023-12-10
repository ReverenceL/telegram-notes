import functools
from typing import Callable

from aiogram_dialog import DialogManager


async def transfer_start_data(start_data: dict, manager: DialogManager):
    if isinstance(start_data, dict):
        manager.dialog_data.update(start_data)


def text_length_filter(text: str, length: int) -> str:
    if len(text) > length:
        raise ValueError
    return text


def get_text_length_filter(length: int) -> Callable[[str], str]:
    return functools.partial(text_length_filter, length=length)
