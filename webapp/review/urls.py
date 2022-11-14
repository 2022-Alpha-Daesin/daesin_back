from review.views import ReviewListAPIView, ReviewRetrieveAPIView
from django.urls import path

urlpatterns = [
    path('', ReviewListAPIView.as_view()),
    path('<int:pk>', ReviewRetrieveAPIView.as_view()),
]
