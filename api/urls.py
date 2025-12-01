from django.urls import path, include

urlpatterns = [
    path('', include('user.user_urls'))
]
