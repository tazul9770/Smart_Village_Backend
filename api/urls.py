from django.urls import path, include
from rest_framework_nested import routers
from profession.views import ProfessionUserViewset
from village.views import ComplainViewSet, ComplainResponseViewSet, EventViewSet

router = routers.DefaultRouter()

router.register('profession_user', ProfessionUserViewset, basename='profession_user')
router.register('complains', ComplainViewSet, basename='complains')
router.register('events', EventViewSet, basename='events')

complain_router = routers.NestedDefaultRouter(router, 'complains', lookup='complain')
complain_router.register('response', ComplainResponseViewSet, basename='complain-response')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(complain_router.urls)),
    path("auth/", include('djoser.urls')),
    path("auth/", include('djoser.urls.jwt'))
]
