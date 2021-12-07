from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/<str:username>/', views.blog, name='blog'),
    path('blog/<str:username>/follow/', views.blog_follow, name='blog_follow'),
    path('blog/<str:username>/unfollow/', views.blog_unfollow,
         name='blog_unfollow'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('follow/', views.follow_index, name='follow_index'),
    path('create/', views.post_create, name='post_create'),
    path('posts/<int:post_id>/edit/', views.post_edit, name='post_edit'),
    path('posts/<int:post_id>/viewed/', views.post_viewed, name='post_viewed'),
    path('posts/<int:post_id>/unviewed/', views.post_unviewed,
         name='post_unviewed')
         ]
