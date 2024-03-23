from rest_framework import routers
from django.urls import path, include, re_path
from courses import views

routers = routers.DefaultRouter()

#tên trên đường dẫn
routers.register('categories',views.CategoryViewSet, basename='categories')


urlpatterns = [
    path('', include(routers.urls)),

]
