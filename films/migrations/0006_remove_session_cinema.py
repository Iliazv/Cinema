# Generated by Django 2.2.14 on 2023-12-09 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0005_auto_20231209_2301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='cinema',
        ),
    ]