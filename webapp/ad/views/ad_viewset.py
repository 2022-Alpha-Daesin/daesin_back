from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from ad.serializers.ad_serializer import ADSerializer
from ad.models import Advertisement


class ADViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = ADSerializer

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user, type="A")

    def perform_update(self, serializer):
        return serializer.save(author=self.request.user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance.post)
        return Response(status=status.HTTP_204_NO_CONTENT)
