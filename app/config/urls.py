from django.urls import include, path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Test Cam API",
        default_version='v1',
        description="Test Cam Description",
        contact=openapi.Contact(email="xoklhyip@yandex.ru"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path('api/', include('user.api.urls')),
    path('api/', include('frame.api.urls')),
    path('api/swagger', schema_view.with_ui('swagger', cache_timeout=0)),
]