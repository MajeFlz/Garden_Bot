from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo

admin_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Начислить баллы', url="https://aiogram.readthedocs.io/_/downloads/en/latest/pdf/")],
    [InlineKeyboardButton(text='Добавить задание', url="https://aiogram.readthedocs.io/_/downloads/en/latest/pdf/")]
])

web_ui = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Запустить приложение', web_app=WebAppInfo(url = "https://majeflz.github.io/WEBAPP/"))],
    [InlineKeyboardButton(text='Инструкция создания кошелька', callback_data="wallet_info")],
    [InlineKeyboardButton(text='О проекте', callback_data="about")]
])
