from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help ="Command to populate required groups."

    def handle(self, *args, **kwargs):
        groups = ['Doctor','Patient','Technician', "Staff", 'Nurse']

        for group in groups:
            Group.objects.get_or_create(name=group)
            