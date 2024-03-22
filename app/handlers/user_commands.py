from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command
from app.keyboards.inline_user import inline_user_menu

user_commands = Router()


@user_commands.message(Command('user_menu'))
async def user_menu(message: Message):
    text = "Меню:"
    await message.answer(text, reply_markup=await inline_user_menu())