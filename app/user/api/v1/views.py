from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework import mixins, viewsets, status
from rest_framework.views import APIView
from user.serializers import UserSerializer
from user.api.v1.responses import LoginResponse, LogoutResponse
from config.permissions import UnauthenticatedPOST
from rest_framework.permissions import IsAuthenticated


class RegistrationUserViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = UserSerializer


class AuthUserView(APIView):
    permission_classes = [IsAuthenticated | UnauthenticatedPOST]

    def post(self, request):

        email = request.data.get('email')
        password = request.data.get('password')
        
        if email is None or password is None:
            return Response({'message': LoginResponse.MISSING}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return Response({'message': LoginResponse.SUCCESS}, status=status.HTTP_200_OK)

        return Response({'message': LoginResponse.INVALID}, status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request):

        logout(request)
        return Response({'message': LogoutResponse.SUCCESS}, status=status.HTTP_200_OK)
