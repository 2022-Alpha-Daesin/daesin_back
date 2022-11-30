from rest_framework.pagination import PageNumberPagination


class ClubPageNumberPagination(PageNumberPagination):
    page_size = 8
