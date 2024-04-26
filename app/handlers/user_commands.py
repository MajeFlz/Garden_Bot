"""
Документация для функции user_menu.

Эта функция отвечает на команду /user_menu, отображая пользователю встроенную клавиатуру с меню.

Args:
    message (aiogram.types.Message): Объект сообщения.

Returns:
    None
"""

from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command
from app.keyboards.inline_user import inline_user_menu

user_commands = Router()

@user_commands.message(Command('user_menu'))
async def user_menu(message: Message):
    """
    Функция для отображения пользователю встроенной клавиатуры с меню при получении команды /user_menu.

    Args:
        message (aiogram.types.Message): Объект сообщения.
    """
    text = "Меню:"
    await message.answer(text, reply_markup=await inline_user_menu())
