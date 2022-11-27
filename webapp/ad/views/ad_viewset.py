from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from ad.models import Advertisement
from ad.serializers.ad_serializer import ADSerializer


class ADViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = ADSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user, type="A")

    def perform_update(self, serializer):
        return serializer.save(author=self.request.user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance.post)
        return Response(status=status.HTTP_204_NO_CONTENT)
