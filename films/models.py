from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
import datetime
from datetime import datetime, timedelta
from .managers import CustomUserManager


date = datetime.now()
current_year = date.year

def small_hall():
    hall = {}
    for i in range(1, 6*6+1):
        hall[i] = False
    return hall

def medium_hall():
    hall = {}
    for i in range(1, 8*8+1):
        hall[i] = False
    return hall

def big_hall():
    hall = {}
    for i in range(1, 10*10+1):
        hall[i] = False
    return hall


class User(AbstractUser):
    email = models.EmailField(_('email'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def get_name(self):
        return self.usernames


class Film(models.Model):
    title = models.CharField(verbose_name='Фильм', max_length=100)
    country = models.CharField(verbose_name='Страна производства', max_length=100)
    creation_year = models.IntegerField(verbose_name='Год создания', default=current_year)
    age = models.IntegerField(verbose_name='Возрастное ограничение', default=0)
    duration = models.DurationField(verbose_name='Продолжительность', default=timedelta)
    description = models.TextField(verbose_name='Описание', max_length=5000)
    director = models.CharField(verbose_name='Режиссер', max_length=80)
    picture = models.ImageField(upload_to='film_images/', verbose_name='Изображение', blank=True)
    preview = models.ImageField(upload_to='film_images/', verbose_name='Превью', blank=True)
    link = models.CharField(verbose_name='Ссылка', max_length=255, default='', blank=True)
    tag = models.CharField(verbose_name='Тег', max_length=80, blank=True)
    subscribe = models.BooleanField(verbose_name='Подписка', default=False)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class Cinema(models.Model):
    name = models.CharField(verbose_name='Название', max_length=100)
    description = models.TextField(verbose_name='Описание', default='', max_length=1500)
    location = models.CharField(verbose_name='Местоположение', max_length=150)
    map = models.CharField(verbose_name='Карта', max_length=600, default='', blank=True)
    slug = models.SlugField(verbose_name='URL', max_length=255, unique=True, db_index=True)
    image = models.ImageField(upload_to='cinema_images', verbose_name='Изображение', blank=True)
    hall = models.IntegerField(verbose_name='Количество залов', default=6)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Кинотеатр'
        verbose_name_plural = 'Кинотеатры'


class Session(models.Model):
    TYPE_CHOICES = (
        ('2D', '2D'),
        ('3D', '3D'),
        ('4D', '4D'),
    )

    film = models.ForeignKey(Film, verbose_name='Фильм', on_delete=models.CASCADE,  default='', related_name='sessions')
    cinema = models.ForeignKey(Cinema, verbose_name='Кинотеатр', on_delete=models.CASCADE, default='', related_name='sessions')
    time = models.DateTimeField(verbose_name='Дата показа', default=datetime.now)
    hall = models.CharField(verbose_name='Зал', max_length=40, default='')
    price = models.DecimalField(verbose_name='Стоимость', max_digits=6, decimal_places=2, default=300)
    type = models.CharField(verbose_name='Технология', max_length=2, default='2D', choices=TYPE_CHOICES)
    place_list = models.JSONField(verbose_name='Места в зале', default=small_hall)

    def __str__(self):
        return f'{self.film.title} - {self.time}'

    class Meta: 
        verbose_name = 'Сессия'
        verbose_name_plural = 'Сессии'


class Genre(models.Model):
    GENRE_CHOICES = (
        ('приключения', 'Приключения'),
        ('триллер', 'Триллер'),
        ('ужасы', 'Ужасы'),
        ('фантастика', 'Фантастика'),
        ('боевик', 'Боевик'),
        ('детектив', 'Детектив'),
        ('комедия', 'Комедия'),
        ('криминал', 'Криминал'),
        ('комедия', 'Комедия'),
        ('драма', 'Драма'),
        ('фэнтези', 'Фэнтези'),
        ('спорт', 'Спорт'),
    )

    film = models.ForeignKey(Film, verbose_name='Фильм', on_delete=models.CASCADE, related_name='genres')
    genre = models.CharField(verbose_name='Жанр', max_length=20, choices=GENRE_CHOICES)
    
    def __str__(self):
        return f'{self.film.title} - {self.genre}'
    
    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    
class Image(models.Model):
    film = models.ForeignKey(Film, verbose_name='Фильм', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(verbose_name='Изображение', upload_to='film_images')

    def __str__(self):
        return f'{self.film.title}'
    
    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class Ticket(models.Model):
    customer = models.ForeignKey(User, verbose_name='Покупатель', on_delete=models.CASCADE, related_name='tickets')
    session = models.ForeignKey(Session, verbose_name='Киносеанс', on_delete=models.CASCADE, related_name='tickets')
    seat_number = models.IntegerField(verbose_name='Номер', default=0)
    price = models.DecimalField(verbose_name='Стоимость', max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return f'{self.session} - {self.customer}'
    
    class Meta:
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'


class Question(models.Model):
    notation = models.CharField(verbose_name='Вопрос', max_length=250)
    text = models.TextField(verbose_name='Текст', max_length=2000)

    def __str__(self):
        return self.notation[:60]
    
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'