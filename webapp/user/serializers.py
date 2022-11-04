from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from user.models import User


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

