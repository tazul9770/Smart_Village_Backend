from django.urls import path, include

urlpatterns = [
    path('', include('user.user_urls')),
    path("auth/", include('djoser.urls')),
    path("auth/", include('djoser.urls.jwt'))
]
