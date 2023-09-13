import aiosqlite

from ...settings import CONFIG
from .base import BaseStorage


class SQLiteStorage(BaseStorage):
    def __init__(self, model: type, connection: aiosqlite.Connection = None, chunk_size: int = 20) -> None:
        self.model = model
        self.conn = connection
        self.chunk_size = chunk_size

    async def get(self, table: str, *args, **kwargs):
        query = f'SELECT * FROM {table}'
        if len(kwargs.values()) > 0:    
            query += f' WHERE {" AND ".join([f"{k} = {v}" for k, v in kwargs.items()])}'

        async with self.conn.cursor() as cursor: 
            await cursor.execute(query)
            rows = await cursor.fetchall()


        print('AAAA', rows)
