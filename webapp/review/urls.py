from review.views.review_list_apiview import ReviewListAPIView, ReviewRetrieveAPIView
from django.urls import path

urlpatterns = [
    path('', ReviewListAPIView.as_view()),
    path('<int:pk>', ReviewRetrieveAPIView.as_view()),
]
