
from rest_framework.decorators import action
from rest_framework import viewsets, generics
from rest_framework.response import Response

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

    #Url: /courses/{course_id}/lessons/?q=
    #Lấy danh sách bài học có ID là pk
    #ếu trên dường dẫn không có {course_id} thì không cần tham số PK
    @action(methods=['get'], detail=True)
    def lessons(self, request, pk):
        course = self.get_object()  # Lấy đối tượng course từ pk
        lessons = course.lesson_set.filter(active=True).all()
        serializer = serializers.LessonSerializer(lessons, many=True, context={'request':request})
        
        return Response(serializer.data)
