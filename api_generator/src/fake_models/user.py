from pydantic import BaseModel, Field

from .base import fake


class FakeUser(BaseModel):
    email: str = Field(default_factory=fake.email)
