from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from notification.models import Notification, Village
from notification.serializers import NotificationSerializer, VillageSerializer

class VillageViewSet(ModelViewSet):
    queryset = Village.objects.all()
    serializer_class = VillageSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        return [IsAuthenticated()]


class NotificationViewSet(ModelViewSet):
    serializer_class = NotificationSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        return [IsAuthenticated()]

    def get_queryset(self):
        return Notification.objects.filter(active=True).order_by('-created_at')
    