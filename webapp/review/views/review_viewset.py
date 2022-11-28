from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from review.serializers import ReviewSerializer,ReviewListSerializer
from review.models import Review


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'list':
            return ReviewListSerializer
        return ReviewSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def perform_create(self, serializer):
        return serializer.save(author=self.request.user,images=self.request.FILES.getlist('images'),tags=self.request.data.getlist('tags'), type="R")
    
    def perform_update(self, serializer):
        return serializer.save(author=self.request.user,images=self.request.FILES.getlist('images'),tags=self.request.data.getlist('tags'))

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance.post)
        return Response(status=status.HTTP_204_NO_CONTENT)
