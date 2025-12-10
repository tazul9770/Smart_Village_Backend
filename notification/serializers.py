from rest_framework import serializers
from notification.models import Notification, Village

class VillageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = Village
        fields = [
            'id',
            'name',
            'description',
            'post_code',
            'image',
            'established_year',
            'head_of_village',
            'population',
            'total_voters',
            'literacy_rate',
            'area_sq_km',
            'number_of_houses',
            'number_of_schools',
            'number_of_health_centers',
            'number_of_markets',
            'number_of_religious_places',
            'number_of_community_centers',
            'has_electricity',
            'has_clean_water',
            'has_internet',
            'created_at',
            'updated_at',
        ]


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'message', 'created_at']



