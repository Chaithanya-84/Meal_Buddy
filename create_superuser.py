import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meal_buddy.settings')
django.setup()

from django.contrib.auth import get_user_model

def main():
    User = get_user_model()
    username = 'admin'
    email = 'admin@example.com'
    password = 'password'
    if User.objects.filter(username=username).exists():
        print('Superuser already exists')
    else:
        User.objects.create_superuser(username, email, password)
        print('Superuser created: username=admin password=password')

if __name__ == '__main__':
    main()
