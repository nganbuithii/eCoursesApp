

from rest_framework import viewsets, generics
from courses import serializers
from courses.models import Category


# Create your views here.

# Tạo serializer đầu tiên
# Đừng kế thừa model viewset -> 6api
class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
