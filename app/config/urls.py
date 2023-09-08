from django.urls import include, path

urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path('api/', include('user.api.urls')),
    path('api/', include('frame.api.urls')),
]