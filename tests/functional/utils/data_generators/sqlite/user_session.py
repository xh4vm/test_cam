from ...fake_models.user_session import FakeUserSession
from .base import BaseSqliteDataGenerator


class UserSessionDataGenerator(BaseSqliteDataGenerator):
    table = "user_session"
    fake_model = FakeUserSession
