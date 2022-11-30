from rest_framework.routers import DefaultRouter

from relationship.views import ScrapViewSet

router = DefaultRouter()
router.register('', ScrapViewSet, basename='Scrap')

urlpatterns = []

urlpatterns += router.urls
