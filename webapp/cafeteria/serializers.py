from rest_framework.serializers import ModelSerializer
from .models import Cafeteria,Menu


class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields =['division','food']

class CafeteriaSerializer(ModelSerializer):
    menus = MenuSerializer(many=True)
    class Meta:
        model =Cafeteria
        fields =['name','menus']