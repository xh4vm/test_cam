from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import mixins, viewsets, status
from rest_framework.views import APIView
from user.models import User
from user.serializers import UserSerializer, ObtainTokenSerializer


class CreateUserViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = UserSerializer


class ObtainTokenView(APIView):
    permission_classes = [AllowAny]
    serializer_class = ObtainTokenSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')

        user = User.objects.filter(email=email).first()
        
        if user is None or not user.check_password(password):
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

        
    

class VerifyTokenView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ObtainTokenSerializer

    def post(self, request):
        pass


class AuthViewSet(APIView):

    # def post(self, request):

    #     if 'email' not in request.data or 'password' not in request.data:
    #         return Response({'message': 'Credentials missing'}, status=status.HTTP_400_BAD_REQUEST)
        
    #     email = request.POST['email']
    #     password = request.POST['password']

    #     user = authenticate(request, email=email, password=password)

    #     if user is not None:
    #         login(request, user)
    #         # auth_data = get_tokens_for_user(request.user)

    #         return Response({'message': 'Login Success'}, status=status.HTTP_200_OK)
    #         # return Response({'message': 'Login Success', **auth_data}, status=status.HTTP_200_OK)

        # return Response({'message': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request):

        logout(request)
        return Response({'message': 'Successfully Logged out'}, status=status.HTTP_200_OK)
