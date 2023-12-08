import os
import django

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cms.settings')  # Replace 'your_project_name' with your actual project
# name

# Initialize Django
django.setup()

from django.contrib.auth.models import User
from faker import Faker

fake = Faker()

for _ in range(3):
    username = fake.user_name()
    email = fake.email()
    password = fake.password()

    User.objects.create_user(
        username=username,
        email=email,
        password=password
    )

print("3 random users have been created.")