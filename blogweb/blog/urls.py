from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_blog, name='create_blog'),
    path('', views.list_blogs, name='list_blogs'),
    path('<int:pk>/', views.blog_detail, name='blog_detail'),
    path('<int:pk>/edit/', views.update_blog, name='update_blog'),
    path('<int:pk>/delete/', views.delete_blog, name='delete_blog'),
    path('signup/', views.signup, name='signup'),
    path('<int:pk>/comment/', views.add_comment, name='add_comment'),

    ]
