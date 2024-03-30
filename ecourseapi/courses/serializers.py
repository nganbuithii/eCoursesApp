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
    # Sửa đường dẫn ảnh
    def to_representation(self, instance):
        req = super().to_representation(instance)
        req['image'] = instance.image.url
        return req

    # image = serializers.SerializerMethodField(source='image')
    tags = TagSerializer(many=True)


class CourseSerializer(BaseSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(BaseSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"

#
class LessonDetailSerializer(LessonSerializer):
    liked = serializers.SerializerMethodField()

    class Meta:
        model = Lesson
        fields = list(LessonSerializer.Meta.fields) + ['liked']

    def get_liked(self, lesson):
        request = self.context.get("request")
        # Kiểm tra xem người dùng đã xác thực hay chưa
        if request and request.user.is_authenticated:
            # Trả về True nếu người dùng đã thích bài học, ngược lại trả về False
            return lesson.like_set.filter(user=request.user, active=True).exists()
        # Trường hợp không xác thực hoặc không có request, trả về False
        return False


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email']
        extra_kwargs = {
            'password': {
                'write_only': True
                # bật cờ này lên thì sẽ không trả mật khẩu về cho user
            }
        }

    # băm mật khẩu
    def create(self, validated_date):
        data = validated_date.copy()

        # ** data: đồng nghĩa lấy hêết keys ở field ra
        user = User(**data)
        user.set_password(data['password'])
        user.save()

        return user


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Comment
        fields = ['id', 'content', 'user']
