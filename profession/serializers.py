from rest_framework import serializers
from profession.models import ProfessionUser

class ProfessionUserSerializer(serializers.ModelSerializer):
    address = serializers.CharField(source='user.address', read_only=True)
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)
    phone_number = serializers.EmailField(source='user.phone_number', read_only=True)

    class Meta:
        model = ProfessionUser
        fields = ['id','first_name','email', 'phone_number','age','image',
                  'address','description','profession',]

    def create(self, validated_data):
        user = self.context['request'].user
        if user.is_anonymous:
            raise serializers.ValidationError("You must be logged in to create a profile.")
        
        if ProfessionUser.objects.filter(user=user).exists():
            raise serializers.ValidationError("You already have a ProfessionUser profile.")

        return ProfessionUser.objects.create(user=user, **validated_data)
