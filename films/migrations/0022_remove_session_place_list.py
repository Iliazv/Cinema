# Generated by Django 4.2 on 2023-12-21 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0021_session_place_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='place_list',
        ),
    ]
