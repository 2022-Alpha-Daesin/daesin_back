from rest_framework.routers import DefaultRouter
from relationship.views import CommentViewSet

router = DefaultRouter()
router.register('', CommentViewSet, basename='Comment')

urlpatterns = []

urlpatterns += router.urls
