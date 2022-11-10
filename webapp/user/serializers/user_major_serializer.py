from rest_framework import serializers
from user.models import UserMajor


class UserMajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMajor
        fields = ['user', 'major', 'number']