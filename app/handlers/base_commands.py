from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command
from app.keyboards.inline_admin import web_ui

base_command = Router()


@base_command.message(Command("start"))
async def start_message(message: Message):
    text = (f'Привет, {message.from_user.first_name}!\n'
            'Я бот который будет выдавать тебе награды за волонтерство в прекрасном саду\n\n'
            'Если тебе потребуется помощь, просто введи команду /help')

    await message.answer(text, reply_markup=web_ui)


@base_command.message(Command("help"))
async def help_message(message:Message):
    text = (f'Ещё в разработке')
    await message.answer(text)
