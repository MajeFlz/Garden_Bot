"""
Документация для класса DbSession.

Этот класс представляет собой middleware для управления подключением к базе данных aiomysql в ходе выполнения запросов бота.

Attributes:
    pool (aiomysql.pool.Pool): Пул подключений к базе данных aiomysql.pool.Pool.
"""

import aiomysql
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from typing import Callable, Dict, Any, Awaitable
from app.utils.dbconnect import Request

class DbSession(BaseMiddleware):
    """
    Middleware для управления подключением к базе данных в ходе выполнения запросов бота.

    Attributes:
        pool (aiomysql.pool.Pool): Пул подключений к базе данных aiomysql.pool.Pool.
    """

    def __init__(self, pool: aiomysql.pool.Pool):
        """
        Инициализация объекта DbSession.

        Args:
            pool (aiomysql.pool.Pool): Пул подключений к базе данных aiomysql.pool.Pool.
        """
        super().__init__()
        self.pool = pool

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        """
        Обработчик вызова, выполняющийся при каждом запросе.

        Args:
            handler (Callable): Обработчик запроса.
            event (TelegramObject): Объект события.
            data (Dict[str, Any]): Данные запроса.

        Returns:
            Any: Результат выполнения обработчика.
        """
        async with self.pool.acquire() as conn:
            data['request'] = Request(conn)
            return await handler(event, data)

