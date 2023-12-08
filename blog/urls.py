from django.urls import path
from .views import *

urlpatterns = [
    path('posts/', list_of_posts, name='list_of_posts'),
    path('drafts/', list_of_drafts, name='list_of_drafts'),
    path('posts/<str:slug>', post_detail, name='post_detail'),
    path('posts/category/<str:category_slug>', category_filter, name='category_filter'),
    path('posts/<slug:slug>/', add_comment, name='add_comment'),
    path('backend/post/new/', add_post, name='add_post'),
    path('posts/author/<str:author_name>', author_filter, name='author_filter'),
]