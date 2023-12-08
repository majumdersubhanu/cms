from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import *

urlpatterns = [
    path('posts/', list_of_posts, name='list_of_posts'),
    path('drafts/', list_of_drafts, name='list_of_drafts'),
    path('posts/<str:slug>', post_detail, name='post_detail'),
    path('posts/category/<str:category_slug>', category_filter, name='category_filter'),
    path('posts/<slug:slug>/', add_comment, name='add_comment'),
    path('backend/posts/new/', add_post, name='add_post'),
    path('backend/posts', list_of_all_posts, name='post_list_backend'),
    path('backend/posts/<slug:slug>/edit', edit_post, name='edit_post'),
    path('backend/posts/<slug:slug>/delete/', delete_post, name='delete_post'),
    path('posts/author/<str:author_name>', author_filter, name='author_filter'),

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
]