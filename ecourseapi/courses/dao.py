from django.db.models import Count

from courses.models import Course, Category, Lesson


def get_courses(**kwargs):
    courses = Course.objects.filter(active=True)

    q = kwargs.get('q')
    if q:
        courses = courses.filter(name__icontains=q)

    cate_id = kwargs.get('category_id')
    if cate_id:
        courses = courses.filter(category_id=cate_id)

    # sắp xếp

    return courses.order_by("-id")
    # giảm theo id


# đếm khóa học theo danh mục
def count_courses_by_cate():
    return Category.objects.annotate(counter=Count('course__id')).values('id', 'name', 'counter').all()
