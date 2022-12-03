from rest_framework.generics import ListAPIView
from django.utils import timezone
from .serializers import CafeteriaSerializer
from .models import Cafeteria
# Create your views here.

class CafeteriaListAPIView(ListAPIView):
    queryset = Cafeteria.objects.filter(date = timezone.now())
    serializer_class = CafeteriaSerializer
