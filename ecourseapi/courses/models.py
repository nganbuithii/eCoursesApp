from django.db import models

# Usser chứng thưc
from django.contrib.auth.models import AbstractUser


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
    description = models.TextField()
    image = models.ImageField(upload_to='courses/%Y/%m/')

    # khóa ngoại
    # PROTECT:lafaf danh mục đến khóa học thì k cho xóa
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
