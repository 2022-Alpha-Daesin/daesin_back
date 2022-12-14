from .base import *

DEBUG = False

# 배포시 로그설정 - 이거 사용하면 배포 안 되던데요?
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'console': {
#             'level': 'DERROR',
#             'filters': None,
#             'class': 'logging.StreamHandler',
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['console'],
#             'level': 'ERROR',
#         },
#     },
# }

URL_FRONT = 'https://daesin.tk/'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get("DATABASES_NAME"),
        'USER': os.environ.get("DATABASES_USER"),
        'PASSWORD': os.environ.get("DATABASES_PASSWORD"),
        'HOST': os.environ.get("DATABASES_HOST"),
        'PORT': '3306',
    }
}