from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand
from app.models import Profile
from datetime import date
from django.utils.crypto import get_random_string

User = get_user_model()
class Command(BaseCommand):
    help = "Create Admin Accoumt"

    def handle(self, *args, **kwargs):
        profile, status = Profile.objects.get_or_create(
            first_name = 'svc',
            last_name = 'account',
            email = 'svc@account.com',
            contact_number = 'xxxxxxxxxx',
            date_of_birth = date(year=1990, day=1, month=1),
            gender = 'other',
            address = 'localhost',
            city = 'xxxx',
            country= 'xxxx',
            zip_code = 'xxxx'
        )
        if status:
            user, status = User.objects.get_or_create(
                email = profile.email,
                Profile = profile
            )
            if status:
                user.first_name = profile.first_name
                user.last_name = profile.last_name
                p = get_random_string(length=10)
                user.set_password(p)
                user.save()

                groups = Group.objects.all()
                for group in groups:
                    group.user_set.add(user)
                print('email : {}, password : {}'.format(profile.email, p))