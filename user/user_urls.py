from django.urls import path
from user.views import test, demo

urlpatterns = [
    path("test/", test),
    path("demo/", demo)
]