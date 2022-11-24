from django.urls import path

from notice.views import NoticeListAPIView

urlpatterns = [
    path('', NoticeListAPIView.as_view()),
]
