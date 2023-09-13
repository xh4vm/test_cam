from pydantic import Field
from typing import Any
from ..make_password.pbkdf2_sha256 import hash_password

from .base import fake, FakeTimestampMixin


class FakeUser(FakeTimestampMixin):
    email: str = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)

    @classmethod
    def main_keys(cls) -> list[str]:
        return ['email']

    def dict(self, *args, **kwargs) -> dict[str, Any]:
        data = super().dict(*args, **kwargs)
        data['password'] = hash_password(self.password)
        return data

    def request_data(self):
        return {
            'email': self.email,
            'password': self.password
        }
