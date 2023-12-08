from django.urls import path
from .views import list_of_posts, post_detail, category_filter, list_of_drafts, add_comment

urlpatterns = [
    path('posts/', list_of_posts, name='list_of_posts'),
    path('drafts/', list_of_drafts, name='list_of_drafts'),
    path('posts/<str:slug>', post_detail, name='post_detail'),
    path('posts/category/<str:category_slug>', category_filter, name='category_filter'),
    path('posts/<str:slug>/', add_comment, name='add_comment'),
]