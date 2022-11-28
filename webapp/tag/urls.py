from rest_framework.routers import DefaultRouter
from tag.views import TagViewSet

router = DefaultRouter()
router.register('', TagViewSet, basename='Tag')

urlpatterns = []

urlpatterns += router.urls
