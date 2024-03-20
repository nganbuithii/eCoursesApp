from django.db import models
from ckeditor.fields import RichTextField
# Usser chứng thưc
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField

class User(AbstractUser):
    pass


# Create your models here.
class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

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
