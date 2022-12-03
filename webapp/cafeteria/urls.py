from django.urls import path

from .views import CafeteriaListAPIView

urlpatterns = [
    path('', CafeteriaListAPIView.as_view()),
]
