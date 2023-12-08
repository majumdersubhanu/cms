from django.contrib import admin

from blog.models import Post, Category, Comment


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'status')
    list_filter = ('published_date', 'category', 'author')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'approved')


admin.site.register(Comment, CommentAdmin)