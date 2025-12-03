from rest_framework.viewsets import ModelViewSet
from api.pagination import DefaultPagination
from village.models import Complain
from village.serializers import ComplainSerializer
from api.permissions import IsAdminOrOwner
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter

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
