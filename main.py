import asyncio
import logging
import asyncpg
from aiogram import Bot, Dispatcher

from app.settings import settings
from app.utils.commands import set_commands
from app.handlers.base_commands import base_command
from app.handlers.user_commands import user_commands
from app.handlers.admin_commands import admin_commands
from app.middlewares.dbmiddleware import DbSession

async def start_bot(bot: Bot):
    await set_commands(bot)

# Раскомментить при наличии готовой БД
# async def db_create_pool():
#     return await asyncpg.create_pool(user='postgres', password='', database='users', host='127.0.0.1', port=5432, command_timeout=60)

async def start() -> None:
    logging.basicConfig(level=logging.INFO)  # на проде отключить из-за нагрузки

    dp = Dispatcher()

    dp.include_routers(
        base_command,
        user_commands,
        admin_commands
    )

    bot = Bot(token=settings.bots.bot_token)

    # Раскомментить при наличии готовой БД
    # try:
    #     pool_connect = await db_create_pool()
    # finally:
    #     print('Ошибка подключения БД')

    #dp.update.middleware.register(DbSession(pool_connect()))
    dp.startup.register(start_bot)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())
