from django.core.management.base import BaseCommand, CommandError
import csv
import datetime
#from sightings.models import Squirrel

class Command(BaseCommand):
    help = 'Import data from csv file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', nargs='+', type=str,help="The path of the source csv file")

    def handle(self, *args, **options):
        file_path = options['file_path'][0]
        
        self.stdout.write(self.style.SUCCESS(f'Today is {datetime.date.today()}'))
        self.stdout.write(self.style.SUCCESS('Successfully get the argument: %s' % file_path))
