from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from .models import *

class CustomUserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        model = User
        fields = ('id','email', 'full_name' ,'birth_year', 'address', 'public_visibility', 'password')