from rest_framework import serializers
from user.models import UserMajor
from . import MajorSerializer


class UserMajorSerializer(serializers.ModelSerializer):
    major = MajorSerializer(read_only=True)
    class Meta:
        model = UserMajor
        fields = ['user', 'major', 'number']