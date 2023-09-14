from ...fake_models.frame import FakeFrame
from .base import BaseSqliteDataGenerator


class FrameDataGenerator(BaseSqliteDataGenerator):
    table = 'frame'
    fake_model = FakeFrame
