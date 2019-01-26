import asyncpg
import settings as settings


class DataBase:
    @staticmethod
    async def initialize():
        conn = await asyncpg.connect(
            dsn=f'postgresql://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}/{settings.DB_NAME}'
        )
