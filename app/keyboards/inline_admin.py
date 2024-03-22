from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

admin_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Начислить баллы', url="https://aiogram.readthedocs.io/_/downloads/en/latest/pdf/")],
    [InlineKeyboardButton(text='Добавить задание', url="https://aiogram.readthedocs.io/_/downloads/en/latest/pdf/")]
])