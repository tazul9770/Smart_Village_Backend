from rest_framework import serializers
from village.models import Complain, ComplainResponse, Event

class EmptySerializer(serializers.Serializer):
    pass

class ComplainSerializer(serializers.ModelSerializer):

    image = serializers.ImageField()

    address = serializers.CharField(source='user.address', read_only=True)
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    phone_number = serializers.EmailField(source='user.phone_number', read_only=True)

    status = serializers.CharField(read_only=True)

    class Meta:
        model = Complain
        fields = ['id', 'first_name', 'address', 'phone_number',
                   'tag', 'title', 'description', 'image', 'status']
        
class UpdateStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complain
        fields = ['status']

class ComplainResponseSerializer(serializers.ModelSerializer):
    responder_name = serializers.CharField(source='responder.first_name', read_only=True)
    complain_title = serializers.CharField(source='complain.title', read_only=True)
    class Meta:
        model = ComplainResponse
        fields = ['id', 'message', 'responder_name', 'complain_title']
        read_only_fields = ['responder_name', 'complain_title']

class EventSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    participant = serializers.StringRelatedField(many=True, read_only=True)
    organizer = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'image',
                   'location', 'category','organizer', 'participant']
        
        