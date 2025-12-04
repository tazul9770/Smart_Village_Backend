from rest_framework.viewsets import ModelViewSet
from api.pagination import DefaultPagination
from village.models import Complain, ComplainResponse, Event
from village.serializers import ComplainSerializer, UpdateStatusSerializer, ComplainResponseSerializer, EventSerializer
from api.permissions import IsAdminOrOwner
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import PermissionDenied
from rest_framework import permissions

class ComplainViewSet(ModelViewSet):
    queryset = Complain.objects.select_related('user').all()
    serializer_class = ComplainSerializer
    pagination_class = DefaultPagination
    filter_backends = [SearchFilter]
    search_fields = ['title', 'tag', 'status']
    permission_classes = [IsAdminOrOwner]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'], url_path='my')
    def my_complains(self, request):
        user = request.user
        queryset = self.get_queryset().filter(user=user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def change_status(self, request, pk=None):
        complain = self.get_object()
        if not request.user.is_staff:
            return Response({"detail": "Only staff can change status."}, status=403)

        status_new = request.data.get('status')
        complain.status = status_new
        complain.save()
        return Response({"detail": f"Status changed to {status_new}"})
    
    def get_serializer_class(self):
        if self.action == 'change_status':
            return UpdateStatusSerializer
        return ComplainSerializer
    
class ComplainResponseViewSet(ModelViewSet):
    serializer_class = ComplainResponseSerializer

    def get_queryset(self):
        complain_id = self.kwargs.get('complain_pk')
        return ComplainResponse.objects.select_related('responder').prefetch_related('complain').filter(complain_id=complain_id)

    def perform_create(self, serializer):
        if not self.request.user.is_staff:
            raise PermissionDenied("Only staff can create a response.")
        complain_id = self.kwargs.get('complain_pk')
        complain = get_object_or_404(Complain, pk=complain_id)
        serializer.save(complain=complain, responder=self.request.user)


class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    pagination_class = DefaultPagination
    filter_backends = [SearchFilter]
    search_fields = ['title', 'category', 'description']

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [permissions.IsAdminUser()]
        else:
            permission_classes = [permissions.IsAuthenticated()]
        return permission_classes

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)

    @action(detail=True, methods=['post', 'get'])
    def join(self, request, pk=None):
        event = self.get_object()
        user = request.user
        if event.status != 'upcoming':
            return Response({'error':"Cannot join completed event"}, status=400)
        if user in event.participant.all():
            return Response({"mesage":"Already join this event"})
        event.participant.add(user)
        return Response({'seccess':'Successfull joined this event'})

    @action(detail=True, methods=['get','post'])
    def leave(self, request, pk=None):
        event = self.get_object()
        user = request.user
        if user in event.participant.all():
            event.participant.remove(user)
            return Response({'message': 'Left event'})
        return Response({'message': 'You are not a participant'})
