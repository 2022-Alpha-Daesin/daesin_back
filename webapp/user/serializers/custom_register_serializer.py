from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers


class CustomRegisterSerializer(RegisterSerializer):
    username = None
    email = serializers.EmailField(required=True)
    nickname = serializers.CharField(max_length=20, required=True)
    grade = serializers.IntegerField(required=False)
    major_id = serializers.IntegerField()

    def get_cleaned_data(self):
        return {
            'email': self.validated_data.get('email', ''),
            'nickname': self.validated_data.get('nickname', ''),
            'grade': self.validated_data.get('grade', ''),
            'major_id': self.validated_data.get('major_id', ''),
            'password1': self.validated_data.get('password1', ''),
        }