from frame.models import Frame
from typing import Any
from jsonschema import validate, ValidationError
from rest_framework.serializers import (
    ModelSerializer,
    DateTimeField,
    Serializer,
    JSONField,
    ValidationError as SerializerValidationError,
)


class FrameSerializer(ModelSerializer):
    TimeSection = DateTimeField(input_formats=["%d-%m-%Y:%H-%M-%S"])

    def validate_cam_id(self, cam_id: int) -> int:
        if not 0 < cam_id < 100:
            raise SerializerValidationError(
                "Cam id value must be into interval (0, 100)"
            )

        return cam_id

    def validate_ChannelNo(self, channel: int) -> int:
        if not 1 <= channel <= 2:
            raise SerializerValidationError(
                "Channel No value must be into interval [1,2])"
            )

        return channel

    def validate_ConfigNo(self, config: int) -> int:
        if not 0 <= config <= 1:
            raise SerializerValidationError(
                "Config No value must be into interval [0,1])"
            )

        return config

    def validate_VideoColor(self, video_frame: dict[str, Any]) -> int:
        schema = {
            "type": "object",
            "properties": {
                "Brightness": {"type": "number", "minimum": 0, "maximum": 100},
                "Contrast": {"type": "number", "minimum": 0, "maximum": 100},
                "Hue": {"type": "number", "minimum": 0, "maximum": 100},
                "Saturation": {"type": "number", "minimum": 0, "maximum": 100},
            },
            "required": ["Brightness", "Contrast", "Hue", "Saturation"],
        }
        try:
            validate(instance=video_frame, schema=schema)
        except ValidationError as error:
            raise SerializerValidationError(str(error))

        return video_frame

    class Meta:
        model = Frame
        fields = (
            "cam_id",
            "VideoColor",
            "TimeSection",
            "ChannelNo",
            "ConfigNo",
        )


class FrameContributorSerializer(Serializer):
    contributors = JSONField()

    def validate_contributors(self, contributors: list[int]) -> list[int]:
        schema = {"type": "array", "items": {"type": "number"}}

        try:
            validate(instance=contributors, schema=schema)
        except ValidationError:
            raise SerializerValidationError("Contributors is array")

        return contributors
