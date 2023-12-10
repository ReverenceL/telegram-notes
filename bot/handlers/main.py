from aiogram import Dispatcher

from bot.handlers import root


def setup_handlers(dp: Dispatcher) -> None:
    dp.include_routers(
        root.router,
    )
