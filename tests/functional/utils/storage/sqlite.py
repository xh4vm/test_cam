import aiosqlite
from typing import Iterable

from ...settings import CONFIG
from .base import BaseStorage


class SQLiteStorage(BaseStorage):
    def __init__(self, model: type, connection: aiosqlite.Connection = None) -> None:
        self.model = model
        self.conn = connection

    async def get(self, table: str, chunk_size: int, *args, **kwargs) -> Iterable[type]:
        fields = self.model.__fields__.keys()
        query = f'SELECT {", ".join(fields)} FROM {table}'

        if len(kwargs.values()) > 0:
            kv = [f"{k} = '{v}'" for k, v in kwargs.items()]  
            query += f' WHERE {" AND ".join(kv)}'

        query += f' LIMIT {chunk_size}'

        async with self.conn.cursor() as cursor: 
            await cursor.execute(query)
            rows = await cursor.fetchall()

        return [self.model(**dict(zip(fields, row))) for row in rows]
    
    async def delete(self, table: str, *args, **kwargs) -> bool:
        if len(kwargs.values()) == 0:
            return False
    
        kv = [f"{k} = '{v}'" for k, v in kwargs.items()]  
        query = f'DELETE FROM {table} WHERE {" AND ".join(kv)}'

        async with self.conn.cursor() as cursor: 
            await cursor.execute(query)
        
        await self.conn.commit()
        return True