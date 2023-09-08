from datetime import datetime, timedelta

import jwt
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed, ParseError


User = get_user_model()


class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        jwt_token = request.META.get('HTTP_AUTHORIZATION')
        if jwt_token is None:
            return None

        jwt_token = JWTAuthentication.get_the_token_from_header(jwt_token)  # clean the token

        try:
            payload = jwt.decode(jwt_token, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.exceptions.InvalidSignatureError:
            raise AuthenticationFailed('Invalid signature')
        except:
            raise ParseError()

        # Get the user from the database
        user_id = payload.get('user_id')
        if user_id is None:
            raise AuthenticationFailed('User id not found in JWT')

        user = User.objects.get(user_id)

        if user is None:
            raise AuthenticationFailed('User not found')

        return user, payload

    def authenticate_header(self, request):
        return 'Bearer'

    @classmethod
    def create_jwt(cls, user):
        payload = {
            'user_id': user.id,
            'exp': int((datetime.now() + timedelta(hours=settings.JWT['TOKEN_LIFETIME_HOURS'])).timestamp()),
            'iat': datetime.now().timestamp(),
            'email': user.email,
        }

        # Encode the JWT with your secret key
        jwt_token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

        return jwt_token

    @classmethod
    def get_the_token_from_header(cls, token):
        token = token.replace('Bearer', '').replace(' ', '')  # clean the token
        return token