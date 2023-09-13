from pydantic import BaseModel, Field

from .base import fake, FakeTimestampMixin


class FakeUser(FakeTimestampMixin):
    email: str = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)
