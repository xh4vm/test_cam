from pydantic import BaseModel, Field

from .base import fake


class FakeUser(BaseModel):
    email: str = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)

    def request_data(self):
        return {
            "email": self.email,
            "password": self.password,
        }
