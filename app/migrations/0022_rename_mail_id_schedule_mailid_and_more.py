# Generated by Django 4.0.4 on 2022-05-25 01:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_schedule_timing'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedule',
            old_name='mail_id',
            new_name='mailid',
        ),
        migrations.RenameField(
            model_name='schedule',
            old_name='ph_no',
            new_name='phno',
        ),
    ]