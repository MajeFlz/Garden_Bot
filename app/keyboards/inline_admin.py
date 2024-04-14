from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo

admin_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Начислить баллы', url="https://aiogram.readthedocs.io/_/downloads/en/latest/pdf/")],
    [InlineKeyboardButton(text='Добавить задание', url="https://aiogram.readthedocs.io/_/downloads/en/latest/pdf/")]
])

web_ui = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Запустить приложение', web_app=WebAppInfo(url = "https://127.0.0.1:3000"))]
])