from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

menu_items = ['Задания', 'Баллы', 'Мероприятия', 'NFTree', 'Загрузить фото']


async def inline_user_menu():
    button_menu = InlineKeyboardBuilder()
    for item in menu_items:
        button_menu.add(InlineKeyboardButton(
            text=item,
            url="https://aiogram.readthedocs.io/_/downloads/en/latest""/pdf/")
        )
    return button_menu.adjust(2).as_markup()
