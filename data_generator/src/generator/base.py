import aiohttp
import json
from abc import ABC, abstractmethod
from loguru import logger
from typing import Iterable, Any

from settings import CONFIG


class BaseDataGenerator(ABC):
    @property
    @abstractmethod
    def fake_model(self):
        """Fake model"""

    @property
    @abstractmethod
    def url(self) -> str:
        """URL"""

    @property
    @abstractmethod
    def schema(self) -> str:
        """JSON schema"""

    @property
    @abstractmethod
    def method(self) -> str:
        """HTTP method"""

    async def _get_fake_data_from_file(self) -> Iterable[dict[str, Any]]:
        with open(f'{CONFIG.BASE_DIR}/schemas/{self.schema}.json', 'r') as fd:
            for _ in json.loads(fd.read()):
                yield _

    async def _get_fake_model(self, fake_data: Iterable[dict[str, Any]]) -> Iterable[dict[str, Any]]:
        async for obj in fake_data:
            yield self.fake_model(**obj)

    async def load(self):
        fake_data = self._get_fake_data_from_file()

        async with aiohttp.ClientSession() as session:
            async for model in self._get_fake_model(fake_data):
                func = getattr(session, self.method.lower())
                async with func(self.url, json=model.dict()) as response:
                    logger.info(f'status: "{response.status}" | response: "{await response.json()}"')
