"""
Документация для функций inline_user_menu и connect_wallet.

Эти функции создают встроенные клавиатуры для меню пользователя и подключения кошелька.

"""

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from pytonconnect import TonConnect

menu_items = ['Задания', 'Баллы', 'Мероприятия', 'NFTree', 'Загрузить фото']

async def inline_user_menu():
    """
    Создает встроенную клавиатуру для меню пользователя.

    Returns:
        InlineKeyboardMarkup: Встроенная клавиатура с пунктами меню.
    """
    button_menu = InlineKeyboardBuilder()
    for item in menu_items:
        button_menu.add(InlineKeyboardButton(
            text=item,
            url="https://aiogram.readthedocs.io/_/downloads/en/latest""/pdf/")
        )
    return button_menu.adjust(2).as_markup()

async def connect_wallet():
    """
    Создает встроенную клавиатуру для подключения кошелька.

    Returns:
        InlineKeyboardMarkup: Встроенная клавиатура с кнопками для выбора кошелька.
    """
    buttons_wallet = InlineKeyboardBuilder()
    wallets_list = TonConnect.get_wallets()
    for wallet in wallets_list:
        buttons_wallet.button(text=wallet['name'], callback_data=f'connect:{wallet["name"]}')
    return buttons_wallet.adjust(1, ).as_markup()
