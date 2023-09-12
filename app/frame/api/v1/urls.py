from django.urls import path, include

from config.routers import OptionalSlashRouter
from .views import VideoFrameViewSet

router = OptionalSlashRouter()
router.register("frame", VideoFrameViewSet, basename="frame")

urlpatterns = [
    path("", include(router.urls)),
]
