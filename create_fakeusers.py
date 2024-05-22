import os
import django
from faker import Faker

# Setup Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'storefront.settings')
django.setup()

from users.models import User

fake = Faker()

def create_random_users(n):
    for _ in range(n):
        firstname = fake.first_name()
        lastname = fake.last_name()
        phone = fake.random_int(min=1000000000, max=9999999999)
        joined_date = fake.date_this_decade()

        user = User(
            firstname=firstname, 
            lastname=lastname, 
            phone=phone, 
            joined_date=joined_date
        )
        user.save()

if __name__ == "__main__":
    create_random_users(1000)
    print("1000 random users created successfully!")
