from rest_framework.pagination import PageNumberPagination


class ReviewPageNumberPagination(PageNumberPagination):
    page_size = 6
