from django.conf import settings
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer
from rest_framework import serializers, exceptions
from django.utils.translation import gettext_lazy as _
from user.models import User
from rest_framework.exceptions import ValidationError
from django.contrib.auth import authenticate, get_user_model
from django.urls import exceptions as url_exceptions

class CustomRegisterSerializer(RegisterSerializer):
    username = serializers.CharField(max_length=10, required=True)
    email = serializers.EmailField(required=True)
    nickname = serializers.CharField(max_length=20, required=True)
    grade = serializers.IntegerField(required=False)
    major = serializers.CharField(max_length=30, required=True)

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'email': self.validated_data.get('email', ''),
            'nickname': self.validated_data.get('nickname', ''),
            'grade': self.validated_data.get('grade', ''),
            'major': self.validated_data.get('major', ''),
            'password1': self.validated_data.get('password1', ''),
        }

class UserAbstractSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'nickname',
            'grade',
            'major',
        ]

