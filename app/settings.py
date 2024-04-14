from environs import Env
from dataclasses import dataclass


@dataclass
class Bots:
    bot_token: str


@dataclass
class Database:
    host: str
    port: int
    user: str
    password: str
    db: str


@dataclass
class Settings:
    bots: Bots
    database: Database


def get_settings(path: str):
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


settings = get_settings('config')
