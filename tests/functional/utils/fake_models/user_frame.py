from .base import FakeTimestampMixin


class FakeUserFrame(FakeTimestampMixin):
    user_id: int
    frame_id: int
