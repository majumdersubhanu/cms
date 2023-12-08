from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from blog.forms import CommentForm
from blog.models import Post, Category, Comment


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
    comments = Comment.objects.filter(post=post)
    template = 'blog/post/post_detail.html'
    context = {'post': post, 'comments': comments}
    return render(request, template, context)


def category_filter(request, category_slug):
    category_slug = Category.objects.get(slug=category_slug)
    posts = Post.objects.filter(category=category_slug)
    template = 'blog/post/list_of_posts.html'
    context = {'posts': posts, 'category': category_slug}
    return render(request, template, context)


def add_comment(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog:post_detail', slug=post.slug)
    else:
        form = CommentForm()
    template = 'blog/post/add_comment.html'
    context = {'form': form}
    return render(request, template, context)