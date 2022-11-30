from rest_framework.pagination import PageNumberPagination


class AdPageNumberPagination(PageNumberPagination):
    page_size = 8
