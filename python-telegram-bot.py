import asyncio
import logging

from update_tasks import update_tasks_in_html
from aiogram import F
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

# Включаем логирование, чтобы не пропустить сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="Токен бота")
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Напишите список заданий седующим сообщением")

@dp.message(F.text)
async def handle_text(message: types.Message):
    tasks = message.text.split("\n")
    update_tasks_in_html(tasks)
    await message.answer('Список задач обновлен.')

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

