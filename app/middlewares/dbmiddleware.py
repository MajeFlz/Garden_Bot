import aiomysql
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from typing import Callable, Dict, Any, Awaitable
from app.utils.dbconnect import Request


class DbSession(BaseMiddleware):
    def __init__(self, pool: aiomysql.pool.Pool):
        super().__init__()
        self.pool = pool

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        async with self.pool.acquire() as conn:
            data['request'] = Request(conn)
            return await handler(event, data)
