from aiogram import Bot
from aiogram.types import Message

# @dp.message_handler(Command("start"), state="*")
# async def start_message(message):
#     text = (f'Привет, {message.from_user.first_name}!\n'
#             'Я бот который будет выдавать тебе награды за волонтерство в прекрасном саду\n\n'
#             'Если тебе потребуется помощь, просто введи команду /help')
#
#
#     markup = await main_menu()
#     await message.answer(text, reply_markup=markup)