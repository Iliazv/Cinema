# Generated by Django 4.2 on 2023-12-29 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0026_alter_session_type_ticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='seat_number',
            field=models.IntegerField(default=0, verbose_name='Номер'),
        ),
    ]