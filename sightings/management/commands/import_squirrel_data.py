from django.core.management.base import BaseCommand, CommandError
import csv
import datetime
from sightings.models import Squirrel

class Command(BaseCommand):
    help = 'Import data from csv file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', nargs='+', type=str,help="The path of the source csv file")

    def handle(self, *args, **options):
        file_path = options['file_path'][0]
        with open(file_path) as f:
            reader = csv.reader(f)
            pass_signal = True
        
            for row in reader:
                if pass_signal:
                    pass_signal = False
                    continue
                else:
                    if row[7] not in ['Adult', 'Juvenile']:
                        r_age = Squirrel.OTHER
                    elif row[7] == 'Adult':
                        r_age = Squirrel.ADULT
                    elif row[7] == 'Juvenile':
                        r_age = Squirrel.JUVENILE
                    
                    if row[8] not in ['Gray', 'Cinnamon','Black']:
                        r_pri_color = Squirrel.OTHER
                    elif row[8] == 'Gray':
                        r_pri_color = Squirrel.GRAY
                    elif row[8] == 'Cinnamon':
                        r_pri_color = Squirrel.CINNAMON
                    elif row[8] == 'Black':
                        r_pri_color = Squirrel.BLACK
                    
                    if row[12] not in ['Ground Plane', 'Above Ground']:
                        r_location = Squirrel.OTHER
                    elif row[12] == 'Ground Plane':
                        r_location = Squirrel.GROUND_PLANE
                    elif row[12] == 'Above Ground':
                        r_location = Squirrel.ABOVE_GROUND
                    
                    _, created = Squirrel.objects.get_or_create(
                        lon=float(row[0]),
                        lat=float(row[1]),
                        squirrel_id=row[2],
                        shift=row[4],
                        date=datetime.date(int(row[5][-4:]),int(row[5][0:2]),int(row[5][2:4])),
                        age=r_age,
                        pri_color=r_pri_color,
                        location=r_location,
                        specific_location=row[14],
                        running=bool(row[15]),
                        chasing=bool(row[16]),
                        climbing=bool(row[17]),
                        eating=bool(row[18]),
                        foraging=bool(row[19]),
                        other_activities=row[20],
                        kuks=bool(row[21]),
                        quaas=bool(row[22]),
                        moans=bool(row[23]),
                        tail_flags=bool(row[24]),
                        tail_twitches=bool(row[25]),
                        approaches=bool(row[26]),
                        indifferent=bool(row[27]),
                        runs_from=bool(row[28])
                        )
            
        self.stdout.write(self.style.SUCCESS('Successfully load data from %s' % file_path))
