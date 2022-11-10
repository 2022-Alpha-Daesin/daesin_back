from rest_framework import serializers
from user.models import Major


class MajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Major
        fields = ['college', 'major']