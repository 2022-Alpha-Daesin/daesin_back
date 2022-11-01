from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
    openapi.Info(
        title='Daesin API',
        default_version='v1',
        description='daesin api',
        contact=openapi.Contact(email='leahpar0401@kookmin.ac.kr'),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


def ping(request):
    return HttpResponse('pong')


urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("ping/", ping),
    path("admin/", admin.site.urls)
]
