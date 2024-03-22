from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command
from app.keyboards.inline_admin import admin_menu

admin_commands = Router()


@admin_commands.message(Command('admin_menu'))
async def admin_menu(message: Message):
    text = "Меню:"
    await message.answer(text, reply_markup=admin_menu)