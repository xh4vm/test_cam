from config.routers import OptionalSlashRouter
from django.urls import include, path

from .views import CreateUserViewSet, AuthViewSet, ObtainTokenView


router = OptionalSlashRouter()
router.register('user/sign_up', CreateUserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('user/auth', AuthViewSet.as_view(), name='auth'),
    path('user/auth/token', ObtainTokenView.as_view(), name='token_obtain_pair'),
]
