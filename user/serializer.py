from djoser.serializers import UserSerializer as BaseUser, UserCreateSerializer as Base

class UserCreateSerializer(Base):
    class Meta(Base.Meta):
        fields = ['id', 'email', 'password', 'first_name',
                  'last_name', 'address', 'phone_number']
        
class UserSerializer(BaseUser):
    class Meta(BaseUser.Meta):
        fields = ['id', 'email', 'first_name',
                  'last_name', 'address', 'phone_number']
