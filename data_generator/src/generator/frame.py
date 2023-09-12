from settings import CONFIG
from .base import BaseDataGenerator
from ..fake_models.frame import FakeFrame


class FrameDataGenerator(BaseDataGenerator):
    method = 'POST'
    url = f'{CONFIG.API.URL}:{CONFIG.API.PORT}{CONFIG.API.PATH}/{CONFIG.API.VERSION}/frame'
    fake_model = FakeFrame
    schema = 'frames'
