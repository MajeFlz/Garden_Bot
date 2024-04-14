from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command
from app.keyboards.inline_admin import web_ui
from app.keyboards.inline_user import connect_wallet
from app.utils.dbconnect import Request

base_command = Router()

@base_command.message(Command("start"))
async def start_message(message: Message, request: Request):
    await request.add_user_data(message.from_user.id, message.from_user.first_name)
    text = (f'Привет, {message.from_user.first_name}!\n'
            'Я бот который будет выдавать тебе награды за волонтерство в прекрасном саду\n\n'
            'Если тебе потребуется помощь, просто введи команду /help')

    await message.answer(text, reply_markup=web_ui)


@base_command.message(Command("help"))
async def help_message(message:Message):
    text = (f'Ещё в разработке')
    await message.answer(text)


@base_command.message(Command("wallet"))
async def wallet_message(message: Message):
    await message.answer(text='Выберите кошелек для подключения', reply_markup= await connect_wallet())
