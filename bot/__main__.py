import asyncio

from aiogram import Bot, Dispatcher

from bot.config import BotConfig, DBConfig, load_config
from bot.db import create_pool
from bot.middlewares import setup_middlewares


async def main():
    bot_config = load_config(BotConfig, "bot")
    bot = Bot(bot_config.token)

    dp = Dispatcher()
    db_pool = create_pool(load_config(DBConfig, "db"))

    setup_middlewares(dp, db_pool)

    await dp.start_polling(bot)


asyncio.run(main())
