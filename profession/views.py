from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from profession.models import ProfessionUser
from profession.serializers import ProfessionUserSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from api.permissions import IsAdminOrOwner
from api.pagination import DefaultPagination
from rest_framework.decorators import action
from rest_framework.response import Response

class ProfessionUserViewset(ModelViewSet):
    queryset = ProfessionUser.objects.select_related('user').all()
    serializer_class = ProfessionUserSerializer
    pagination_class = DefaultPagination
    permission_classes = [IsAdminOrOwner]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['age', 'user__first_name', 'user__phone_number', 'profession']
    ordering_fields = ['age', 'user__first_name']

    @action(detail=False, methods=['get'], url_path='by-profession')
    def get_by_profession(self, request):
        profession = request.query_params.get('profession')
        if not profession:
            return Response({"message":"profession parameter is required"})
        queryset = self.get_queryset().filter(profession=profession)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
