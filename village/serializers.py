from rest_framework import serializers
from village.models import Complain

class ComplainSerializer(serializers.ModelSerializer):

    address = serializers.CharField(source='user.address', read_only=True)
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    phone_number = serializers.EmailField(source='user.phone_number', read_only=True)

    status = serializers.CharField(read_only=True)

    class Meta:
        model = Complain
        fields = ['id', 'first_name', 'address', 'phone_number',
                   'tag', 'title', 'description', 'image', 'status']
        