from ...fake_models.user import FakeUser
from .base import BaseSqliteDataGenerator


class UserDataGenerator(BaseSqliteDataGenerator):
    table = 'user'
    fake_model = FakeUser
