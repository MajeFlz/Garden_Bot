"""
Бот Telegram для обработки команд пользователей.

Модуль содержит функции для запуска бота и установки соединения с базой данных.

Автор: NFTree
"""

import asyncio
import logging
import aiomysql
from aiogram import Bot, Dispatcher

from app.settings import settings
from app.utils.commands import set_commands
from app.handlers.base_commands import base_command
from app.handlers.user_commands import user_commands
from app.handlers.admin_commands import admin_commands
from app.middlewares.dbmiddleware import DbSession

async def start_bot(bot: Bot):
    """
    Устанавливает команды бота.

    :param bot: Экземпляр aiogram.Bot для установки команд.
    """
    await set_commands(bot)

async def db_create_pool():
    """
    Создает пул соединений с базой данных MySQL.

    :return: Пул соединений с базой данных.
    """
    return await aiomysql.create_pool(**settings.database.__dict__, autocommit=True)

async def start() -> None:
    """
    Запускает бота Telegram и подключается к базе данных.

    :return: None
    """
    logging.basicConfig(level=logging.INFO)  # На продакшне необходимо отключить из-за нагрузки

    dp = Dispatcher()

    dp.include_routers(
        base_command,
        user_commands,
        admin_commands
    )

    bot = Bot(token=settings.bots.bot_token)

    pool_connect = await db_create_pool()

    dp.update.middleware.register(DbSession(pool_connect))
    dp.startup.register(start_bot)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start())

