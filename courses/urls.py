# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),  
    path('course/create/', views.create_course, name='create_course'),  
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),  
]
