# myapp/context_processors.py

from django.contrib.auth.models import User

from blog.models import Category


def user_context(request):
    user = User.objects.all()
    return {'all_users': user}


def categories_context(request):
    categories = Category.objects.all()
    return {'categories': categories}