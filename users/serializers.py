from rest_framework import serializers
from .models import Userss
from rest_framework.authtoken.models import Token

class UserSerializier(serializers.ModelSerializer):
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        Token.objects.create(user=user)
        return user

    class Meta:
        model = Userss
        fields = ('username', 'password', 'is_noob', 'is_elite', 'is_superuser', 'main_currency')
        extra_kwargs = {'password': {'write_only': True}}