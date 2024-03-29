import json
import aiosqlite
from abc import abstractmethod
from typing import Any
from loguru import logger

from functional.settings import CONFIG

from ..base import BaseDataGenerator


class BaseSqliteDataGenerator(BaseDataGenerator):
    """Генерации фейковых данных, которые используются для тестов."""

    conn = None
    data = []

    @property
    @abstractmethod
    def table(self) -> str:
        """Наименование таблицы"""

    def __init__(self, conn: aiosqlite.Connection, chunk_size: int = 50) -> None:
        self.conn: aiosqlite.Connection = conn
        self.chunk_size: int = chunk_size

    async def load(self):
        fake_data: list[type] = []
        data: list[type] = []

        with open(f"{CONFIG.BASE_DIR}/testdata/{self.table}.json", "r") as fd:
            fake_data = json.load(fd)

        for elem in fake_data:
            model = self.fake_model.parse_obj(elem)
            data.append(model)

        await self._save_data(data=data)

        self.data = data

        return data

    async def clean(self):
        query = f"DELETE FROM {self.table}"

        async with self.conn.cursor() as cursor:
            await cursor.execute(query)

        await self.conn.commit()

    def _get_values_statement(
        self, data: type, fields: list[str] | None = None
    ) -> tuple[Any]:
        fields: list[str] = fields or [
            field for field in self.fake_model.__fields__.keys()
        ]

        try:
            data_as_dict: dict[str, Any] = data.dict()
        except:
            logger.error("Oops")
        return tuple(data_as_dict[key] for key in fields)

    async def _save_data(self, data: dict[str, Any]) -> None:
        into_statement: list[str] = [
            field for field in self.fake_model.__fields__.keys()
        ]
        values = (self._get_values_statement(data=elem) for elem in data)

        insert_query: str = (
            f"INSERT INTO {self.table} "
            f'({", ".join(into_statement)}) '
            f'VALUES ({", ".join(["?" for i in range(len(into_statement))])})'
        )

        async with self.conn.cursor() as cursor:
            await cursor.executemany(insert_query, values)

        await self.conn.commit()

        logger.debug(f"Success multiple insert {self.table} ({len(self.data)} objects)")
