from settings import CONFIG
from .base import BaseDataGenerator
from ..fake_models.user import FakeUser


class UserLoginsDataGenerator(BaseDataGenerator):
    method = "POST"
    url = f"{CONFIG.API.URL}:{CONFIG.API.PORT}{CONFIG.API.PATH}/{CONFIG.API.VERSION}/user/auth"
    fake_model = FakeUser
    schema = "user_logins"
