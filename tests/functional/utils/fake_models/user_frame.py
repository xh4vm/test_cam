from .base import FakeTimestampMixin, FakeBaseMixin, FakeIDMixin


class FakeUserFrame(FakeBaseMixin, FakeIDMixin, FakeTimestampMixin):
    user_id: int
    frame_id: int
