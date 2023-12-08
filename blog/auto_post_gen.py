import os
import django
from faker.generator import random

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cms.settings')  # Replace 'your_project_name' with your actual project
# name

# Initialize Django
django.setup()

from django.contrib.auth.models import User
from django.utils import timezone
from faker import Faker
from blog.models import Post, Category

fake = Faker()

for _ in range(15):
    author = random.choice(User.objects.all())
    title = fake.sentence()
    slug = fake.slug()
    content = fake.paragraphs(nb=5, )
    seo_title = fake.sentence()
    seo_description = fake.paragraph()
    published_date = timezone.now()
    status = random.choice(['draft', 'published'])
    category = random.choice(Category.objects.all())

    Post.objects.create(
        title=title,
        slug=slug,
        content=content,
        seo_title=seo_title,
        seo_description=seo_description,
        author=author,
        published_date=published_date,
        status=status,
        category=category
    )

print("10 posts have been created.")