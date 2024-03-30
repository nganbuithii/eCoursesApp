from rest_framework import routers
from django.urls import path, include, re_path
from courses import views

routers = routers.DefaultRouter()

#tên trên đường dẫn
routers.register('categories',views.CategoryViewSet, basename='categories')
routers.register('courses', views.CourseViewSet, basename='courses')
routers.register('lessons', views.LessonViewSet, basename='lessons')

routers.register('comments', views.CommentViewSet, basename='comments')

routers.register('users', views.UserViewSet, basename='users')

urlpatterns = [
    path('', include(routers.urls)),

]
