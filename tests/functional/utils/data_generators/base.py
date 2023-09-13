from abc import ABC, abstractmethod


class BaseDataGenerator(ABC):
    @property
    @abstractmethod
    def fake_model(self) -> type:
        """Fake model"""

    @property
    @abstractmethod
    def conn(self):
        """Datastore connector"""

    @property
    def data(self) -> list[type]:
        """Сгенерированные фейковые данные"""

    @property
    def response_data(self) -> list[type]:
        """Данные ответа"""

    @abstractmethod
    async def load(self) -> list[type]:
        """Метод загрузки тестовых данных в хранилище"""

    @abstractmethod
    async def clean(self) -> None:
        """Метод удаления тестовых данных из хранилища"""

    def __init__(self, conn) -> None:
        self.conn = conn
