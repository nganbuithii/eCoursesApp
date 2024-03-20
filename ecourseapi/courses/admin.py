import cloudinary
from django.contrib import admin
from courses.models import Course, Category

# đánh dấu mã an toàn
from django.utils.html import mark_safe

# Register your models here.
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


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


# trang quản trị
admin.site.register(Category)
admin.site.register(Course, Coursedmin)
