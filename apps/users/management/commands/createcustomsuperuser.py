# your_app_name/management/commands/createcustomsuperuser.py

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

class Command(BaseCommand):
    help = 'Create a superuser with specified environment variables'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        username = os.getenv('DJANGO_SUPERUSER_USERNAME')
        email = os.getenv('DJANGO_SUPERUSER_EMAIL')
        password = os.getenv('DJANGO_SUPERUSER_PASSWORD')

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f'Superuser "{username}" created successfully'))
        else:
            self.stdout.write(self.style.WARNING(f'Superuser "{username}" already exists'))
