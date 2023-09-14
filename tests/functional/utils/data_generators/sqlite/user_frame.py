from ...fake_models.user_frame import FakeUserFrame
from .base import BaseSqliteDataGenerator


class UserFrameDataGenerator(BaseSqliteDataGenerator):
    table = "user_frame"
    fake_model = FakeUserFrame
