from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from pytonconnect import TonConnect

menu_items = ['Задания', 'Баллы', 'Мероприятия', 'NFTree', 'Загрузить фото']


async def inline_user_menu():
    button_menu = InlineKeyboardBuilder()
    for item in menu_items:
        button_menu.add(InlineKeyboardButton(
            text=item,
            url="https://aiogram.readthedocs.io/_/downloads/en/latest""/pdf/")
        )
    return button_menu.adjust(2).as_markup()


async def connect_wallet():
    buttons_wallet = InlineKeyboardBuilder()
    wallets_list = TonConnect.get_wallets()
    for wallet in wallets_list:
        buttons_wallet.button(text=wallet['name'], callback_data=f'connect:{wallet["name"]}')
    return buttons_wallet.adjust(1, ).as_markup()

