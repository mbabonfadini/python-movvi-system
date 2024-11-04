from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size: int = 10
    max_page_size: int = 100