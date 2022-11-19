from rest_framework import viewsets, mixins, status
from relationship.models import Like
from relationship.serializers import LikeSerializer
from django.db.models import Q
from rest_framework.response import Response


class LikeViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        if Like.objects.filter(Q(user=self.request.user) & Q(post=self.request.POST['post'])).exists():
            return Response(
                {
                    'error': '사용자가 이미 좋아요를 눌렀습니다.'
                 }
            )
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
