from rest_framework.pagination import PageNumberPagination


#phân trang cho khóa học
class CoursePaginator(PageNumberPagination):
    page_size = 2
    # page_size_query_param = 'page_size'
    # max_page_size = 10000