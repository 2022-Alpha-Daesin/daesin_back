from rest_framework.routers import DefaultRouter
from post.views import PostViewSet

router = DefaultRouter()
router.register('', PostViewSet, basename='Post')

urlpatterns = []

urlpatterns += router.urls
