from .base import FakeTimestampMixin, FakeBaseMixin


class FakeUserFrame(FakeBaseMixin, FakeTimestampMixin):
    user_id: int
    frame_id: int
