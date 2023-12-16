from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from blog.forms import CommentForm, PostForm
from blog.models import Post, Category, Comment

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def list_of_posts(request):
    posts = Post.objects.filter(status='published')
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        if int(page) > paginator.num_pages:
            posts = paginator.page(paginator.num_pages)
        else:
            posts = paginator.page(1)
    context = {'posts': posts, 'page': page}
    template = 'blog/post/list_of_posts.html'
    return render(request, template, context)


def list_of_drafts(request):
    posts = Post.objects.filter(status='draft')
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        if int(page) > paginator.num_pages:
            posts = paginator.page(paginator.num_pages)
        else:
            posts = paginator.page(1)
    context = {'posts': posts}
    template = 'blog/post/list_of_posts.html'
    return render(request, template, context)


def list_of_all_posts(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 10)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        if int(page) > paginator.num_pages:
            posts = paginator.page(paginator.num_pages)
        else:
            posts = paginator.page(1)
    context = {'posts': posts}
    template = 'blog/list_of_posts_unfiltered.html'
    return render(request, template, context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = Comment.objects.filter(post=post).filter(approved=True)
    context = {'post': post, 'comments': comments}

    if post.status == 'published':
        template = 'blog/post/post_detail.html'
        return render(request, template, context)
    else:
        template = 'blog/post/post_preview.html'
        return render(request, template, context)


def category_filter(request, category_slug):
    category_slug = Category.objects.get(slug=category_slug)
    posts = Post.objects.filter(category=category_slug)
    template = 'blog/post/list_of_posts.html'
    context = {'posts': posts, 'category': category_slug}
    return render(request, template, context)


def author_filter(request, author_name):
    author_name = author_name.lower()
    author = get_object_or_404(User, username=author_name)
    posts = Post.objects.filter(author=author)
    template = 'blog/post/list_of_posts.html'
    context = {'posts': posts, 'author': author_name}
    return render(request, template, context)


def add_comment(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user.username
            comment.save()
            return redirect('blog:post_detail', slug=post.slug)
    else:
        form = CommentForm()
    template = 'blog/post/add_comment.html'
    context = {'form': form}
    return render(request, template, context)


###########
# BACKEND
###########
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:post_detail', slug=post.slug)
    else:
        form = PostForm()
    template = 'blog/new_post.html'
    context = {'form': form}
    return render(request, template, context)


def edit_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('blog:post_list_backend')
    else:
        form = PostForm(instance=post)
    template = 'blog/new_post.html'
    context = {'form': form}
    return render(request, template, context)


def delete_post(request, slug):
    # if not request.user.is_staff or not request.user.is_superuser:
    #     raise Http404
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    messages.success(request, 'Successfully deleted post')
    return redirect('blog:post_list_backend')


@login_required
def home(request):
    return render(request, "success.html", {})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('blog:post_list_backend')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})