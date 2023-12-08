from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from blog.models import Post, Category


# Create your views here.
def list_of_posts(request):
    posts = Post.objects.filter(status='published')
    context = {'posts': posts}
    template = 'blog/post/list_of_posts.html'
    return render(request, template, context)


def list_of_drafts(request):
    posts = Post.objects.filter(status='draft')
    context = {'posts': posts}
    template = 'blog/post/list_of_posts.html'
    return render(request, template, context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    template = 'blog/post/post_detail.html'
    context = {'post': post}
    return render(request, template, context)


def category_filter(request, category_slug):
    category_slug = Category.objects.get(slug=category_slug)
    posts = Post.objects.filter(category=category_slug)
    template = 'blog/post/list_of_posts.html'
    context = {'posts': posts}
    return render(request, template, context)