from dj_rest_auth.serializers import LoginSerializer
from rest_framework import serializers


class CustomLoginSerializer(LoginSerializer):
    # username = serializers.CharField(required=False, allow_blank=True)
    email = serializers.CharField(required=True, allow_blank=False)
    password = serializers.CharField(style={'input_type': 'password'})
