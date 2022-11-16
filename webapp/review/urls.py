from review.views.review_list_apiview import ReviewListAPIView
from review.views.review_retrieve_apiview import ReviewRetrieveAPIView
from django.urls import path

urlpatterns = [
    path('', ReviewListAPIView.as_view()),
    path('<int:pk>', ReviewRetrieveAPIView.as_view()),
]
