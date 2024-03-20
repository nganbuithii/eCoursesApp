from django.contrib import admin
from courses.models import Course, Category
# Register your models here.

# trang quản trị
admin.site.register(Category)
admin.site.register(Course)