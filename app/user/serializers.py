from user.models import User
from rest_framework.serializers import ModelSerializer, Serializer, CharField


class UserSerializer(ModelSerializer):

    def create(self, data):

        return User.objects.create_user(
            email=data.get('email'),
            password=data.get('password'),
        )

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'password',
        )


class ObtainTokenSerializer(Serializer):
    email = CharField()
    password = CharField()
