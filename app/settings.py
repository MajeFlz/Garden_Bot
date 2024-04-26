"""
Документация для конфигурационного скрипта.

Этот скрипт использует библиотеку Environs для загрузки настроек из файла .env и их представления в виде объектов классов.

"""

from environs import Env
from dataclasses import dataclass

@dataclass
class Bots:
    """
    Класс для представления настроек ботов.

    Attributes:
        bot_token (str): Токен бота.
    """
    bot_token: str

@dataclass
class Database:
    """
    Класс для представления настроек базы данных.

    Attributes:
        host (str): Адрес хоста базы данных.
        port (int): Порт базы данных.
        user (str): Имя пользователя базы данных.
        password (str): Пароль пользователя базы данных.
        db (str): Название базы данных.
    """
    host: str
    port: int
    user: str
    password: str
    db: str

@dataclass
class Settings:
    """
    Класс для представления всех настроек.

    Attributes:
        bots (Bots): Настройки ботов.
        database (Database): Настройки базы данных.
    """
    bots: Bots
    database: Database

def get_settings(path: str):
    """
    Функция для получения настроек из файла .env.

    Args:
        path (str): Путь к файлу .env.

    Returns:
        Settings: Объект класса Settings с загруженными настройками.
    """
    env = Env()
    env.read_env(path)

    return Settings(
        bots=Bots(
            bot_token=env.str("TOKEN")
        ),
        database=Database(
            host=env.str("MYSQL_HOST"),
            port=env.int("MYSQL_PORT"),
            user=env.str("MYSQL_USER"),
            password=env.str("MYSQL_PASSWORD"),
            db=env.str("MYSQL_DB")
        )
    )

# Загрузка настроек из файла .env и сохранение их в переменной settings
settings = get_settings('config')
