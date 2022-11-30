from rest_framework.routers import DefaultRouter

from relationship.views import LikeViewSet

router = DefaultRouter()
router.register('', LikeViewSet, basename='Like')

urlpatterns = []

urlpatterns += router.urls
