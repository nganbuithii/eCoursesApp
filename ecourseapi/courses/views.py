

from rest_framework import viewsets, generics
from courses import serializers, paginators
from courses.models import Category, Course


# Create your views here.

# Tạo serializer đầu tiên
# Đừng kế thừa model viewset -> 6api
class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer

class CourseViewSet(viewsets.ViewSet, generics.ListAPIView):
    # lấy các khóa học active
    queryset = Course.objects.filter(active=True).all()
    serializer_class = serializers.CourseSerializer
    pagination_class = paginators.CoursePaginator

    def get_queryset(self):
        queries = self.queryset

        #chặn lại để tìm theo keywor /?q=..
        q = self.request.query_params.get("q")
        if q:
            queries = queries.filter(name__icontains=q)

        # Lọc theo category_id
        category_id = self.request.query_params.get("category")
        if category_id:
            queries = queries.filter(category=category_id)

        return queries

