from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('blog/create/', views.blog_create, name='blog_create'),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('blog/<int:pk>/update/', views.blog_update, name='blog_update'),
    path('blog/<int:pk>/delete/', views.blog_delete, name='blog_delete'),

    path('post/create/', views.post_create, name='post_create'),
    path('post/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/update/', views.post_update, name='post_update'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),

    path('category/create/', views.category_create, name='category_create'),
    path('category/', views.category_list, name='category_list'),
    path('category/<int:pk>/', views.category_detail, name='category_detail'),
    path('category/<int:pk>/update/', views.category_update, name='category_update'),
    path('category/<int:pk>/delete/', views.category_delete, name='category_delete'),

    path('tag/create/', views.tag_create, name='tag_create'),
    path('tag/', views.tag_list, name='tag_list'),
    path('tag.<int:pk>/', views.tag_detail, name='tag_detaile'),
    path('tag/<int:pk>/update/', views.tag_update, name='tag_update'),
    path('tag/<int:pk>/delete/', views.tag_delete, name='tag_delete'),
]