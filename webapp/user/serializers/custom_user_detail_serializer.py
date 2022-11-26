from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers
from . import UserMajorSerializer
from user.models import UserMajor
from django.contrib.auth import get_user_model
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
