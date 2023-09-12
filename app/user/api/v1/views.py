from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework import mixins, viewsets, status
from rest_framework.views import APIView
from user.serializers import UserSerializer
from user.api.v1.responses import LoginResponse, LogoutResponse, RegistrationResponse
from config.permissions import UnauthenticatedPOST
from config.serializers import BaseResponseSerializer
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class RegistrationUserViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = UserSerializer

    @swagger_auto_schema(responses={201: BaseResponseSerializer()})
    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return Response(
            {"message": RegistrationResponse.SUCCESS}, status=status.HTTP_201_CREATED
        )


class AuthUserView(APIView):
    permission_classes = [IsAuthenticated | UnauthenticatedPOST]

    @swagger_auto_schema(
        request_body=UserSerializer,
        responses={
            201: BaseResponseSerializer(),
            400: BaseResponseSerializer(),
            401: BaseResponseSerializer(),
        },
    )
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        if email is None or password is None:
            return Response(
                {"message": LoginResponse.MISSING}, status=status.HTTP_400_BAD_REQUEST
            )

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return Response(
                {"message": LoginResponse.SUCCESS}, status=status.HTTP_200_OK
            )

        return Response(
            {"message": LoginResponse.INVALID}, status=status.HTTP_401_UNAUTHORIZED
        )

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter("X-CSRFToken", openapi.IN_HEADER, type=openapi.IN_HEADER)
        ]
    )
    def delete(self, request):
        logout(request)
        return Response({"message": LogoutResponse.SUCCESS}, status=status.HTTP_200_OK)
