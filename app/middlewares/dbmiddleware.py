from typing import Callable, Dict, Any, Awaitable
from app.utils.dbconnect import Request
import asyncpg
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject


class DbSession(BaseMiddleware):
    def __init__(self, connector: asyncpg.pool.Pool):
        super().__init__()
        self.connector = connector

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
            async with self.connector.acquire() as connect:
                data['request'] = Request(connect)
                return await handler(event, data)
