from user.models import User
from rest_framework.serializers import (
    ModelSerializer,
    ValidationError as SerializerValidationError,
)
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


class UserSerializer(ModelSerializer):
    def create(self, data):
        return User.objects.create_user(
            email=data.get("email"), password=data.get("password")
        )

    def validate_password(self, password: str) -> str:
        try:
            validate_password(password)
        except ValidationError as error:
            raise SerializerValidationError(error.messages)

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "password",
        )
