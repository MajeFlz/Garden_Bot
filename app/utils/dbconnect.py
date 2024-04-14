import aiomysql


class Request:
    def __init__(self, connector: aiomysql.Connection):
        self.connector = connector

    async def add_user_data(self, user_id, user_name):
        query = (
            f"INSERT INTO users (user_id, user_name) "
            f"VALUES ({user_id}, '{user_name}') "
            f"ON DUPLICATE KEY UPDATE user_name = '{user_name}'"
        )
        async with self.connector.cursor() as cursor:
            await cursor.execute(query)

