# Generated by Django 4.0.4 on 2022-05-23 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_alter_schedule_ph_no'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Schedule',
        ),
    ]