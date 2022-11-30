from rest_framework.pagination import PageNumberPagination


class ScrapPageNumberPagination(PageNumberPagination):
    page_size = 4


class CommentPageNumberPagination(PageNumberPagination):
    page_size = 2

