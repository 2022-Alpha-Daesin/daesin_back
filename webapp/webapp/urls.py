from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from dj_rest_auth.registration.views import VerifyEmailView
from user.views import ConfirmEmailView

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
    return HttpResponse('pong!!!!!!!')

urlpatterns = [

    path('', include('dj_rest_auth.urls')),
    path('registration/', include('dj_rest_auth.registration.urls')),
    # 유효한 이메일이 유저에게 전달
    re_path(r'^account-confirm-email/$', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    # 유저가 클릭한 이메일(=링크) 확인
    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', ConfirmEmailView.as_view(), name='account_confirm_email'),

    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # 임시 url
    path("ping/", ping),
    path("admin/", admin.site.urls)

]
