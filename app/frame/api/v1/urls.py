from django.urls import path

from .views import VideoFrameView

urlpatterns = [
    path('frame', VideoFrameView.as_view(), name='frame'),
]
