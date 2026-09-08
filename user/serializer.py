from djoser.serializers import UserSerializer as BaseUser, UserCreateSerializer as Base
from rest_framework import serializers
from user.models import Contact

class UserCreateSerializer(Base):
    class Meta(Base.Meta):
        fields = ['id', 'email', 'password', 'first_name',
                  'last_name', 'address', 'phone_number']
        
class UserSerializer(BaseUser):
    image = serializers.ImageField(required=False)
    class Meta(BaseUser.Meta):
        fields = ['id', 'email', 'first_name',
                  'last_name', 'address', 'phone_number', 'image', 'is_staff']
        read_only_fields=['is_staff']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'email', 'phone_number', 'comment']

    def validate_phone_number(self, number):
        if not number.isdigit():
            raise serializers.ValidationError("Phone number must contain only digits")
        if len(number) != 11:
            raise serializers.ValidationError("Phone number must be exactly 11 digits.")
        return number
