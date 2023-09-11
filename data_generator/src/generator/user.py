from settings import CONFIG
from .base import BaseDataGenerator
from ..fake_models.user import FakeUser


class UserDataGenerator(BaseDataGenerator):
    method = 'POST'
    url = f'{CONFIG.API.URL}:{CONFIG.API.PORT}{CONFIG.API.PATH}/{CONFIG.API.VERSION}/user/registration'
    fake_model = FakeUser
    schema = 'users'
