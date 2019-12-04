from django.db import models
from django.utils.translation import gettext as _

class Squirrel(models.Model):
    lat = models.FloatField(
            help_text = _('Latitude'),
            )
    
    lon = models.FloatField(
            help_text = _('Longitude'),
            )
    
    squirrel_id = models.CharField(
            max_length = 1000,
            help_text = _('Unique Squirrel ID'),
            unique = True,
            )
    
    PM = 'PM'
    AM = 'AM'
    SHIFT_CHOICES = (
            (PM,'PM'),
            (AM,'AM'),
            )
    shift = models.CharField(
            max_length=2,
            choices=SHIFT_CHOICES,
            default=AM,
            )
    
    date = models.DateField(
            help_text = _('Date'),
            )
    
    ADULT = 'adult'
    JUVENILE = 'juvenile'
    OTHER = 'other' 
    AGE_CHOICES = (
            (ADULT,'Adult'),
            (JUVENILE,'Juvenile'),
            (OTHER,'Other'),
            )
    age = models.CharField(
            max_length=20,
            choices=AGE_CHOICES,
            default=OTHER,
            )
    
    GRAY = 'gray'
    CINNAMON = 'cinnamon'
    BLACK = 'black'
    PRI_COLOR_CHOICES = (
            (GRAY,'Gray'),
            (CINNAMON,'Cinnamon'),
            (BLACK,'Black' ),
            (OTHER,'Other'),
            )
    pri_color = models.CharField(
            max_length=20,
            choices=PRI_COLOR_CHOICES,
            default=OTHER,
            )
    
    GROUND_PLANE = 'ground plane'
    ABOVE_GROUND = 'above ground'
    LOCATION_CHOICES = (
            (GROUND_PLANE,'Ground Plane'),
            (ABOVE_GROUND,'Above Ground'),
            (OTHER,'Other'),
            )
    location = models.CharField(
            max_length=30,
            choices=LOCATION_CHOICES,
            default=OTHER,
            )
    
    specific_location=models.CharField(
            max_length = 1000,
            help_text = _('specific location of squirrel'),
            blank = True,
            )
    
    running = models.BooleanField(
            help_text = _('whether the squirrel is running'),
            default=False,
            )
    
    chasing = models.BooleanField(
            help_text = _('whether the squirrel is chasing'),
            default=False,
            )
    
    climbing = models.BooleanField(
        help_text = _('whether the squirrel is climbing'),
        default=False,
        )
    
    eating = models.BooleanField(
        help_text = _('whether the squirrel is eating'),
        default=False,
        )
    
    foraging = models.BooleanField(
        help_text = _('whether the squirrel is foraging'),
        default=False,
        )
    
    other_activities = models.CharField(
            max_length = 1000,
            help_text = _('other actions of squirrel besides running, chasing, climbing, eating and foraging'),
            blank = True,
            )
    
    kuks = models.BooleanField(
        help_text = _('whether the squirrel is in kuks'),
        default=False,
        )
    
    quaas = models.BooleanField(
        help_text = _('whether the squirrel is in Quaas'),
        default=False,
        )
    
    moans = models.BooleanField(
        help_text = _('whether the squirrel is in Moans'),
        default=False,
        )
    
    tail_flags = models.BooleanField(
        help_text = _('whether the squirrel has tail flags'),
        default=False,
        )
    
    tail_twitches = models.BooleanField(
        help_text = _('whether the squirrel has tail twitches'),
        default=False,
        )
    
    approaches = models.BooleanField(
        help_text = _('whether approaches or not'),
        default=False,
        )
    
    indifferent = models.BooleanField(
        help_text = _('whether indifferent or not'),
        default=False,
        )
    
    runs_from = models.BooleanField(
        help_text = _('squirrel runs from or not'),
        default=False,
        )
    
    def __str__(self):
        return self.squirrel_id
    
