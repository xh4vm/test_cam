from random import randint
from datetime import datetime
from pydantic import BaseModel, Field
from typing import Any


class FakeFrame(BaseModel):
    cam_id: int = Field(default_factory=lambda: randint(1, 99))
    VideoColor: dict[str, Any] = Field(
        default_factory=lambda: {
            "Brightness": randint(0, 100),
            "Contrast": randint(0, 100),
            "Hue": randint(0, 100),
            "Saturation": randint(0, 100),
        }
    )
    TimeSection: str = Field(
        default_factory=lambda: datetime.utcnow().strftime("%d-%m-%Y:%H-%M-%S")
    )
    ChannelNo: int = Field(default_factory=lambda: randint(1, 2))
    ConfigNo: int = Field(default_factory=lambda: randint(0, 1))
    contributors: list[int] = Field(
        default_factory=lambda: [randint(1, 100) for i in range(randint(1, 10))]
    )

    def request_data(self):
        return {
            "cam_id": self.cam_id,
            "VideoColor": self.VideoColor,
            "TimeSection": self.TimeSection,
            "ChannelNo": self.ChannelNo,
            "ConfigNo": self.ConfigNo,
        }
