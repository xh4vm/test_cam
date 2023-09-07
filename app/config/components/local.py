import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, '..', 'static')

INTERNAL_IPS = [
    '127.0.0.1',
]
CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.1:8080',
    'http://localhost:8080',
]

AUTH_USER_MODEL = "user.User"

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'config.paginators.DefaultPaginator',
    'PAGE_SIZE': 50,
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

JWT = {
    'TOKEN_LIFETIME_HOURS': 5
}