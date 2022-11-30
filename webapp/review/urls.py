from rest_framework.routers import DefaultRouter

from review.views import ReviewViewSet

router = DefaultRouter()
router.register('', ReviewViewSet, basename='Review')

urlpatterns = []

urlpatterns += router.urls
