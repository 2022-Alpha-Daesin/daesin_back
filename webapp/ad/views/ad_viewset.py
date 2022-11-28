from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from ad.models import Advertisement
from ad.permissions import IsAdAuthorOrReadOnly
from ad.serializers import ADSerializer,AdvertisementListSerializer


class ADViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    permission_classes = [IsAdAuthorOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'list':
            return AdvertisementListSerializer
        return ADSerializer
    
    def perform_create(self, serializer):
        return serializer.save(author=self.request.user,images=self.request.FILES.getlist('images'),tags=self.request.data.getlist('tags'), type="A")

    def perform_update(self, serializer):
        return serializer.save(author=self.request.user,images=self.request.FILES.getlist('images'),tags=self.request.data.getlist('tags'))

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance.post)
        return Response(status=status.HTTP_204_NO_CONTENT)
