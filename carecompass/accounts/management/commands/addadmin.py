from django.core.management.base import BaseCommand
from accounts.models import User 

class Command(BaseCommand):
    help = 'Creates a new admin user'

    def handle(self, *args, **kwargs):
        email = input("Enter admin's email: ")
        password = input("Enter admin's password: ")
        first_name = input("Enter admin's first name: ")
        last_name = input("Enter admin's last name: ")

        admin_user = User.objects.create_administrator(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        self.stdout.write(self.style.SUCCESS(f'Admin {admin_user.email} created successfully'))
