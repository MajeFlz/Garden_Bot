"""
Документация для функции set_commands.

Эта функция устанавливает команды бота.

Args:
    bot (aiogram.Bot): Объект бота aiogram.Bot.
"""

from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault

async def set_commands(bot: Bot):
    """
    Устанавливает команды для бота.

    Args:
        bot (aiogram.Bot): Объект бота aiogram.Bot.
    """
    commands = [
        BotCommand(
            command='start',
            description='Начало работы'
        ),
        BotCommand(
            command='help',
            description='Помощь'
        ),
        BotCommand(
            command='user_menu',
            description='Меню волонтера'
        ),
        BotCommand(
            command='admin_menu',
            description='Меню администратора'
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())
