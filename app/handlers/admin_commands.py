"""
Документация для функции admin_menu.

Эта функция отвечает на команду /admin_menu, отображая администратору встроенную клавиатуру с меню.

Args:
    message (aiogram.types.Message): Объект сообщения.

Returns:
    None
"""

from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command
from app.keyboards.inline_admin import admin_menu

admin_commands = Router()

@admin_commands.message(Command('admin_menu'))
async def admin_menu(message: Message):
    """
    Функция для отображения администратору встроенной клавиатуры с меню при получении команды /admin_menu.

    Args:
        message (aiogram.types.Message): Объект сообщения.
    """
    text = "Меню:"
    await message.answer(text, reply_markup=admin_menu)
