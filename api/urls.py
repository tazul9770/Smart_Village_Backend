from django.urls import path, include
from rest_framework_nested import routers
from profession.views import ProfessionUserViewset
from village.views import ComplainViewSet

router = routers.DefaultRouter()

router.register('profession_user', ProfessionUserViewset, basename='profession_user')
router.register('complains', ComplainViewSet, basename='complains')

urlpatterns = [
    path('', include(router.urls)),
    path("auth/", include('djoser.urls')),
    path("auth/", include('djoser.urls.jwt'))
]
