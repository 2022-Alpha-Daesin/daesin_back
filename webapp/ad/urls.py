from rest_framework.routers import DefaultRouter
from ad.views.ad_viewset import ADViewSet

router = DefaultRouter()
router.register('', ADViewSet, basename='AD')

urlpatterns = []

urlpatterns += router.urls
