from frame.models import Frame
from jsonschema import validate
from rest_framework.serializers import (
    ModelSerializer,
    DateTimeField,
    Serializer,
    JSONField,
)


class FrameSerializer(ModelSerializer):
    TimeSection = DateTimeField(input_formats=["%d-%m-%Y:%H-%M-%S"])

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
        validate(instance=contributors, schema=schema)
        return contributors
