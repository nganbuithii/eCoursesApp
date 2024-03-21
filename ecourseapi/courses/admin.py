import cloudinary
from django.contrib import admin
from django.http import request
from django.template.response import TemplateResponse
from django.urls import path

from courses.models import Course, Category, Lesson, Tag

# đánh dấu mã an toàn
from django.utils.html import mark_safe

# Register your models here.
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


# nhúng Tag vào các model khác
class TagInlineAdmin(admin.TabularInline):
    model = Course.tags.through


class CourseForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Course
        fields = '__all__'


# Custom trang quản trị
class Coursedmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'active', 'created_date', 'updated_date']
    search_fields = ['name']
    list_filter = ['id', 'name']
    readonly_fields = ['my_image']
    form = CourseForm
    inlines = [TagInlineAdmin]

    def my_image(self, course):
        if course.image:
            # debug import pdb   pdb.set_trace()
            if type(course.image) is cloudinary.CloudinaryResource:
                return mark_safe(f"<img width='300' src='{course.image.url}'>")
        return mark_safe(f"<img width='300' src='/static/{course.image.name}'>")

    # gắn css
    class Media:
        css = {
            'all': ['/static/css/style.css']
        }


# Trang admin SITE
class CourseAppAdminSite(admin.AdminSite):
    site_header = 'HỆ THỐNG KHÓA HỌC TRỰC TUYẾN'

    def get_urls(self):
        return [path('course-stats/', self.stats_view)] + super().get_urls()

    def stats_view(self, request):  # Thêm tham số 'request' vào đây
        return TemplateResponse(request, 'admin/stats.html')



#định nghĩa trang admin
admin_site = CourseAppAdminSite(name='myadmin')

# trang quản trị
admin_site.register(Category)
admin_site.register(Lesson)
admin_site.register(Tag)
admin_site.register(Course, Coursedmin)
