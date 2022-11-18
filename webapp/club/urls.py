from club.views import ClubListAPIView, ClubRetrieveAPIView
from django.urls import path

urlpatterns = [
        path('', ClubListAPIView.as_view()),
        path('<int:pk>', ClubRetrieveAPIView.as_view())
    ]
