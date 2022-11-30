from rest_framework import serializers

from user.models import Major


class MajorSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='get_full_major', read_only=True)
    name = serializers.CharField(source='get_half_major', read_only=True)

    class Meta:
        model = Major
        fields = ['id', 'name', 'full_name']
