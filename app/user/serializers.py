from user.models import User
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.password_validation import validate_password


class UserSerializer(ModelSerializer):
    def create(self, data):
        validate_password(data.get("password"))

        return User.objects.create_user(
            email=data.get("email"), password=data.get("password")
        )

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "password",
        )
