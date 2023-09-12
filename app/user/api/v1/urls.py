from config.routers import OptionalSlashRouter
from django.urls import include, path

from .views import RegistrationUserViewSet, AuthUserView


router = OptionalSlashRouter()
router.register("user/registration", RegistrationUserViewSet, basename="user")

urlpatterns = [
    path("", include(router.urls)),
    path("user/auth", AuthUserView.as_view(), name="auth"),
]
