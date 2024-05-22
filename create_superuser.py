import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'storefront.settings')
django.setup()

User = get_user_model()

username = 'admin'
password = 'render@1234@5678'
email = 'admin@example.com'

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print('Superuser created successfully.')
else:
    print('Superuser already exists.')
