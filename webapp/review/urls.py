from rest_framework.routers import DefaultRouter
from review.views.review_viewset import ReviewViewSet

router = DefaultRouter()
router.register('', ReviewViewSet, basename='Review')

urlpatterns = []

urlpatterns += router.urls
