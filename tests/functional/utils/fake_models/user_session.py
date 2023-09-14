from datetime import datetime
from .base import FakeBaseMixin


class FakeUserSession(FakeBaseMixin):
    session_key: str
    session_data: str
    expire_date: datetime
    user_id: int
