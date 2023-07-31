import json

from django.core.management import call_command
from django.core.management.base import BaseCommand
from people.models import Person, Address

class Command(BaseCommand):
    help = 'Loads sample data into the database'

    def handle(self, *args, **options):
        # Clear the database
        call_command('flush', '--noinput')

        with open('sample_data.json') as f:
            people_data = json.load(f)

        for person_data in people_data:
            address_data = person_data.pop('address')
            address = Address.objects.create(**address_data)
            Person.objects.create(address=address, **person_data)

        self.stdout.write(self.style.SUCCESS('Successfully loaded sample data'))
