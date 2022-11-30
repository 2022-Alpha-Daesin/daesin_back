from dj_rest_auth.serializers import UserDetailsSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers

from user.models import UserMajor
from . import UserMajorSerializer

UserModel = get_user_model()


class CustomUserDetailSerializer(UserDetailsSerializer):
    user_majors = serializers.SerializerMethodField()

    class Meta:
        fields = ('pk', 'email', 'nickname', 'grade', 'user_majors')
        model = UserModel

    def get_user_majors(self, obj):
        usermajor_query = UserMajor.objects.filter(user=obj)
        serializer = UserMajorSerializer(usermajor_query, many=True)
        return serializer.data
