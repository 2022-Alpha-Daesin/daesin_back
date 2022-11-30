from django.urls import path

from club.views import ClubListAPIView, ClubRetrieveAPIView

urlpatterns = [
    path('', ClubListAPIView.as_view()),
    path('<int:pk>', ClubRetrieveAPIView.as_view())
]
