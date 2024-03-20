from django.db import models
from ckeditor.fields import RichTextField
# Usser chứng thưc
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField


class User(AbstractUser):
    avatar = CloudinaryField(null=True)


# Create your models here.
class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True
        ordering = ['-id']


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    icon = models.CharField(max_length=20, default='tag')

    def __str__(self):
        return self.name


class Course(BaseModel):
    name = models.CharField(max_length=100)
    description = RichTextField()
    image = CloudinaryField()

    # khóa ngoại
    # PROTECT:lafaf danh mục đến khóa học thì k cho xóa
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Tag(BaseModel):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Lesson(BaseModel):
    subject = models.CharField(max_length=255)
    content = RichTextField()
    image = CloudinaryField()
    # trong 1 khóa học không có 2 ba trùng tên
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    class Meta:
        unique_together = ('subject', 'course')


class Interaction(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class Like(Interaction):
    #like theo kiểu facebook
    class Meta:
        unique_together = ("lesson","user")

class Comment(Interaction):
    content = models.CharField(max_length=255)
