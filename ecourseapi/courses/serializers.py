from courses.models import *
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']
class BaseSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(source='image')
    tags = TagSerializer(many=True)

class CourseSerializer(BaseSerializer):

    def get_image(self, course):
        request = self.context.get('request')
        if request:
            # Thay vì truy cập vào thuộc tính name, bạn có thể sử dụng public_id hoặc url hoặc bất kỳ trường nào khác cần thiết từ đối tượng image
            return f"https://res.cloudinary.com/dp0daqkme/image/upload/{course.image.public_id}.png"
        return '/static/%s' % course.image.public_i

    class Meta:
        model = Course
        fields = "__all__"

class LessonSerializer(BaseSerializer):
    def get_image(self, lesson):
        request = self.context.get('request')
        if request:
            # Tương tự như trong CourseSerializer, bạn có thể thay đổi logic xử lý hình ảnh ở đây
            return f"https://res.cloudinary.com/dp0daqkme/image/upload/{lesson.image.public_id}.png"
        return '/static/%s' % lesson.image.public_id
    class Meta:
        model = Lesson
        fields = "__all__"




