# Generated by Django 4.2 on 2023-12-19 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0017_cinema_image_alter_user_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='cinema',
            name='hall',
            field=models.IntegerField(default=6, verbose_name='Количество залов'),
        ),
    ]
