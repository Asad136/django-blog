from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_blog, name='create_blog'),
    path('', views.list_blogs, name='list_blogs'),
    path('<int:pk>/', views.blog_detail, name='blog_detail'),
]
