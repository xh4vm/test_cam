from django.urls import path

from .views import VideoFrameView, UserVideoFrameView

urlpatterns = [
    path('frame', VideoFrameView.as_view(), name='frame'),
    path('frame/user', UserVideoFrameView.as_view(), name='user_frame'),
]
