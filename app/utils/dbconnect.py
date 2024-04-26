"""
Документация для класса Request.

Этот класс представляет собой запрос к базе данных для добавления данных о пользователе.

Attributes:
    connector (aiomysql.Connection): Объект подключения к базе данных aiomysql.Connection.
"""

import aiomysql

class Request:
    """
    Класс для выполнения запросов к базе данных.

    Attributes:
        connector (aiomysql.Connection): Объект подключения к базе данных aiomysql.Connection.
    """

    def __init__(self, connector: aiomysql.Connection):
        """
        Инициализация объекта Request.

        Args:
            connector (aiomysql.Connection): Объект подключения к базе данных aiomysql.Connection.
        """
        self.connector = connector

    async def add_user_data(self, user_id, user_name):
        """
        Асинхронный метод для добавления данных о пользователе в базу данных.

        Args:
            user_id: Идентификатор пользователя.
            user_name: Имя пользователя.
        """
        query = (
            f"INSERT INTO users (user_id, user_name) "
            f"VALUES ({user_id}, '{user_name}') "
            f"ON DUPLICATE KEY UPDATE user_name = '{user_name}'"
        )
        async with self.connector.cursor() as cursor:
            await cursor.execute(query)


