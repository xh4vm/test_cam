import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, '..', 'static')

INTERNAL_IPS = [
    '127.0.0.1',
]
CORS_ALLOWED_ORIGINS = os.environ.get('CORS_ALLOWED_ORIGINS').split(',')
CORS_EXPOSE_HEADERS = ['Content-Type', 'X-CSRFToken']
CORS_ALLOW_CREDENTIALS = True

AUTH_USER_MODEL = "user.User"

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'config.paginators.DefaultPaginator',
    'PAGE_SIZE': 50,
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ),
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ],
}

CSRF_COOKIE_SAMESITE = 'Strict'
SESSION_COOKIE_SAMESITE = 'Strict'
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_HTTPONLY = True
CSRF_TRUSTED_ORIGINS = os.environ.get('CORS_ALLOWED_ORIGINS').split(',')

# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True