from rest_framework.decorators import action
from rest_framework import viewsets, generics, parsers, permissions, status
from rest_framework.response import Response

from courses import serializers, paginators, perms
from courses.models import Category, Course, Lesson, User, Comment, Like

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

        # chặn lại để tìm theo keywor /?q=..
        if self.action.__eq__('list'):
            q = self.request.query_params.get("q")
            if q:
                queries = queries.filter(name__icontains=q)

            # Lọc theo category_id
            category_id = self.request.query_params.get("category")
            if category_id:
                queries = queries.filter(category=category_id)

        return queries

    # Url: /courses/{course_id}/lessons/?q=
    # Lấy danh sách bài học có ID là pk
    # ếu trên dường dẫn không có {course_id} thì không cần tham số PK
    @action(methods=['get'], url_path='lessons', detail=True)
    def lessons(self, request, pk):
        lessons = self.get_object().lesson_set.filter(active=True)
        q = request.query_params.get('q')
        if q:
            lessons = lessons.filter(subject__icontains=q)
        serializer = serializers.LessonSerializer(lessons, many=True, context={'request': request})

        return Response(serializer.data)


class LessonViewSet(viewsets.ViewSet, generics.RetrieveAPIView):
    queryset = Lesson.objects.filter(active=True).all()
    serializer_class = serializers.LessonDetailSerializer
    permission_classes = [permissions.AllowAny]# cho ai cũng có quền xem

    #phải chứng thực mới vào đc
    def get_permissions(self):
        if self.action in ['add_comment', 'like']:
           return [permissions.IsAuthenticated()]
        return self.permission_classes

    # Url: /lessons/{lesson_id}/comments/
    @action(methods=['post'], url_path="comments", detail=True)
    def add_comment(self, request, pk):
        c = Comment.objects.create(user=request.user,
                                   lesson=self.get_object(),
                                   content= request.data.get('content'))
        return Response(serializers.CommentSerializer(c).data, status=status.HTTP_201_CREATED)

    # Url: /lessons/{lesson_id}/like/
    #có detail = True, thì có Pk
    @action(methods=['post'], url_path="like", detail=True)
    def like(self, request, pk):
        # Lấy hoặc tạo một đối tượng Like
        like, created = Like.objects.get_or_create(user=request.user, lesson=self.get_object())

        # Nếu không phải lần đầu tiên thực hiện like, thì cập nhật trạng thái ngược lại
        if not created:
            like.active = not like.active
            like.save()

        #trả ra bài học đã like
        return Response(serializers.LessonDetailSerializer(self.get_object(), context={'request':request}).data, status=status.HTTP_200_OK)





# Đăng kí người dùng
class UserViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = User.objects.filter(is_active=True).all()
    serializer_class = serializers.UserSerializer
    parser_classes = [parsers.MultiPartParser]

    def get_permissions(self):
        if self.action.__eq__('current_user'):
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    @action(methods=['get'], url_name='current_user', detail=False)
    def current_user(selfs, request):
        # tất cả thông tin chứng thực trong requesst.user
        return Response(serializers.UserSerializer(request.user).data)


class CommentViewSet(viewsets.ViewSet,generics.DestroyAPIView, generics.UpdateAPIView):
    #Xoas comment => DestroyAPI
    #cập nhật comments => Update => PUT, PATCH
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [perms.OwnerAuthenticated]