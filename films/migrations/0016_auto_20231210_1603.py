# Generated by Django 2.2.14 on 2023-12-10 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0015_auto_20231210_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='price',
            field=models.DecimalField(decimal_places=2, default=300, max_digits=6, verbose_name='Стоимость'),
        ),
    ]