# Generated by Django 2.2.14 on 2023-12-09 23:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0004_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('location', models.CharField(max_length=150, verbose_name='Местоположение')),
                ('map', models.CharField(blank=True, default='', max_length=255, verbose_name='Карта')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Кинотеатр',
                'verbose_name_plural': 'Кинотеатры',
            },
        ),
        migrations.AlterField(
            model_name='film',
            name='link',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Ссылка'),
        ),
        migrations.AddField(
            model_name='session',
            name='cinema',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.PROTECT, related_name='cinemas', to='films.Cinema', verbose_name='Кинотеатр'),
        ),
    ]
