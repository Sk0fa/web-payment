from api.db import DataBase


class Api:
    def __init__(self):
        self.app = None
        self.db = None

    async def init_connection(self, app):
        self.db = DataBase()
        self.app = app
        await self.db.initialize()
