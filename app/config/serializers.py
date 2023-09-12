from rest_framework.serializers import Serializer


class BaseResponseSerializer(Serializer):
    message: str