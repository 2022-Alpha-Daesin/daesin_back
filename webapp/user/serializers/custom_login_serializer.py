from dj_rest_auth.serializers import LoginSerializer
from rest_framework import serializers,exceptions
from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
from django.urls import exceptions as url_exceptions
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class CustomLoginSerializer(LoginSerializer):
    # username = serializers.CharField(required=False, allow_blank=True)
    email = serializers.CharField(required=True, allow_blank=False)
    password = serializers.CharField(style={'input_type': 'password'})

 