from faker import Faker
from pydantic import BaseModel, Field
from datetime import datetime

fake = Faker()

class FakeTimestampMixin(BaseModel):
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

