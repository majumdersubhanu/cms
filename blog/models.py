from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


# Create your models here.

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    content = models.TextField()
    seo_title = models.CharField(max_length=255, blank=True, null=True)
    seo_description = models.TextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', default=None)
    published_date = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='category', blank=True, null=True)

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ('title',)
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        get_latest_by = 'published_date'

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def get_absolute_url(self):
        return reverse('blog:category_filter', kwargs={'category_slug': self.slug})

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def approve(self):
        self.approved = True
        self.save()

    def __str__(self):
        return self.user