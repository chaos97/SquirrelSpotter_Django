# Generated by Django 2.2.7 on 2019-11-25 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Squirrel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField(help_text='Latitude')),
                ('lon', models.FloatField(help_text='Longitude')),
                ('squirrel_id', models.CharField(help_text='Unique Squirrel ID', max_length=1000)),
                ('shift', models.CharField(choices=[('PM', 'PM'), ('AM', 'AM')], default='AM', max_length=2)),
                ('date', models.DateField(help_text='Date')),
                ('age', models.CharField(choices=[('adult', 'Adult'), ('juvenile', 'Juvenile'), ('other', 'Other')], default='other', max_length=20)),
                ('pri_color', models.CharField(choices=[('gray', 'Gray'), ('cinnamon', 'Cinnamon'), ('black', 'Black'), ('other', 'Other')], default='other', max_length=20)),
                ('location', models.CharField(choices=[('ground plane', 'Ground Plane'), ('above ground', 'Above Ground'), ('other', 'Other')], default='other', max_length=30)),
                ('specific_location', models.CharField(help_text='specific location of squirrel', max_length=1000)),
                ('running', models.BooleanField(default=False, help_text='whether the squirrel is running')),
                ('chasing', models.BooleanField(default=False, help_text='whether the squirrel is chasing')),
                ('climbing', models.BooleanField(default=False, help_text='whether the squirrel is climbing')),
                ('eating', models.BooleanField(default=False, help_text='whether the squirrel is eating')),
                ('foraging', models.BooleanField(default=False, help_text='whether the squirrel is foraging')),
                ('other_activities', models.CharField(help_text='other actions of squirrel besides running, chasing, climbing, eating and foraging', max_length=1000)),
                ('kuks', models.BooleanField(default=False, help_text='whether the squirrel is in kuks')),
                ('quaas', models.BooleanField(default=False, help_text='whether the squirrel is in Quaas')),
                ('moans', models.BooleanField(default=False, help_text='whether the squirrel is in Moans')),
                ('tail_flags', models.BooleanField(default=False, help_text='whether the squirrel has tail flags')),
                ('tail_twitches', models.BooleanField(default=False, help_text='whether the squirrel has tail twitches')),
                ('approaches', models.BooleanField(default=False, help_text='whether approaches or not')),
                ('indifferent', models.BooleanField(default=False, help_text='whether indifferent or not')),
                ('runs_from', models.BooleanField(default=False, help_text='squirrel runs from or not')),
            ],
        ),
    ]