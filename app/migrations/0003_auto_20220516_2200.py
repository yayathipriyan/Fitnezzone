# Generated by Django 3.0.14 on 2022-05-16 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20220516_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(db_column='Email', max_length=100, primary_key=True, serialize=False),
        ),
    ]
