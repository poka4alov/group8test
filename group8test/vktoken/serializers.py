from rest_framework import serializers
from .models import VkUser


class VkUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = VkUser
        fields = ['id', 'password', 'login', 'phone']


class VkTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = VkUser
        fields = ['date_time', 'token']

