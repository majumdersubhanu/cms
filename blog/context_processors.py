# myapp/context_processors.py

from django.contrib.auth.models import User

from blog.models import Category


def user_context(request):
    author = User.objects.all()
    user = request.user
    return {'authors': author, 'user': user}


def categories_context(request):
    categories = Category.objects.all()
    return {'categories': categories}