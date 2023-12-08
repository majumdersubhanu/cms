import os
import django
from faker.generator import random
from faker.providers import internet

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cms.settings')  # Replace 'your_project_name' with your actual project
# name

# Initialize Django
django.setup()

from blog.models import Category
from faker import Faker

fake = Faker()

categories = ["Technology", "Travel", "Food", "Fashion", "Health", "Science", "Fitness", "Books", "Movies", "Music"]

for category in categories:
    Category.objects.create(
        name=category,
        slug=category.lower(),
    )

print(f"{len(categories)} categories have been created.")