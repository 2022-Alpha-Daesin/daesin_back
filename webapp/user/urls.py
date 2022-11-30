from rest_framework.routers import DefaultRouter

from user.views import MajorViewSet, UserMajorViewSet

router = DefaultRouter()
router.register('major', MajorViewSet, basename='Major')
router.register('usermajor', UserMajorViewSet, basename='UserMajor')

urlpatterns = []

urlpatterns += router.urls
