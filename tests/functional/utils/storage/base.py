from abc import abstractmethod, ABC



class BaseStorage(ABC):

    @abstractmethod
    async def get(self, *args, **kwargs):
        """Получение данных"""
