import asyncio

from aiogram import Bot, Dispatcher
from aiogram_dialog import setup_dialogs as setup_aiogram_dialogs

from bot.config import BotConfig, DBConfig, load_config
from bot.db import create_pool
from bot.handlers.main import setup_handlers
from bot.middlewares import setup_middlewares
from bot.dialogs import setup_dialogs


async def main():
    bot_config = load_config(BotConfig, "bot")
    bot = Bot(bot_config.token)

    dp = Dispatcher()
    db_pool = create_pool(load_config(DBConfig, "db"))

    setup_middlewares(dp, db_pool)
    setup_handlers(dp)
    setup_dialogs(dp)
    setup_aiogram_dialogs(dp)

    await dp.start_polling(bot)


asyncio.run(main())
