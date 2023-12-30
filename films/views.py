import json
import django
from django.core import serializers
from django.shortcuts import render, redirect
from .models import Film, Session, Question, User, Cinema, Ticket
from datetime import datetime, timedelta
from django.db.models.functions import TruncDate
from django.db.models import Count
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.template import RequestContext
from django.utils.safestring import SafeString
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import SignupForm

def get_genres():
    genres = (
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
    return genres

def is_ajax(request):
  return request.headers.get('x-requested-with') == 'XMLHttpRequest'

def check_modal(request):
    modal = request.session.get('modal', 'none')
    try: 
        del request.session['modal']
    except KeyError:
        pass
    return modal

def check_session_id(request):
    id = request.session.get('session_id', 'none')
    try: 
        del request.session['session_id']
    except KeyError:
        pass
    return id

def index(request):
    modal = check_modal(request)
    films = Film.objects.filter(subscribe=False)
    films_with_session = Film.objects.annotate(sessions_count=Count("sessions")).filter(sessions_count__gt=0)

    start_date = datetime.now()
    end_date = datetime.now() + timedelta(days=7)
    week_films = []
    for film in films_with_session:
        first_session = film.sessions.order_by('time').last()
        if start_date < first_session.time < end_date:
            week_films.append(film)
            
    soon_films = films.filter(tag='В продаже')
    subscribe_films = Film.objects.filter(subscribe=True)
    context = {'form': SignupForm(), 'week_films': week_films, 'soon_films': soon_films, 'subscribe_films': subscribe_films, 'modal': modal}
    return render(request, 'films/index.html', context)

def film_page(request, pk):
    if request.method == "POST":
        session_pk = request.POST.get('session_pk')
        selected_session = Session.objects.get(pk=session_pk)
        csrf_token = django.middleware.csrf.get_token(request)
        html = render_to_string('films/hall.html', {'selected_session': selected_session, 'request': request, 'csrf_token': csrf_token})
        return JsonResponse({'data': html})
    else:
        modal = check_modal(request)
        film = Film.objects.get(pk=pk)
        session_list = film.sessions.all().order_by('time')
        context = {'form': SignupForm(), 'film': film, 'session_list': session_list, 'modal': modal, 'pk': pk}
        return render(request, 'films/film_page.html', context)

def cinema_page(request, slug):
    modal = check_modal(request)
    cinema = Cinema.objects.get(slug=slug)
    context = {'form': SignupForm(), 'cinema': cinema, 'modal': modal}
    return render(request, 'films/cinema_page.html', context)

def contact(request):
    context = {}
    return render(request, 'films/contact.html', context)

def login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = authenticate(request, email=email, password=password)
    if user is not None:
        auth_login(request, user)
        return redirect('registered')
    else:
        request.session['modal'] = 'login'
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'index'))
    
def logout_view(request):
    logout(request)
    context = {}
    return redirect('index')

def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            auth_login(request, user)
            return redirect('registered')
        
    if request.user.is_authenticated:
        return reverse('index')
    else:
        request.session['modal'] = 'register'
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'index'))
    
@login_required
def registered(request):
    modal = check_modal(request)
    films = Film.objects.filter(subscribe=False)
    films_with_session = Film.objects.annotate(sessions_count=Count("sessions")).filter(sessions_count__gt=0)

    start_date = datetime.now()
    end_date = datetime.now() + timedelta(days=7)
    week_films = []
    for film in films_with_session:
        first_session = film.sessions.order_by('time').last()
        if start_date < first_session.time < end_date:
            week_films.append(film)
            
    soon_films = films.filter(tag='В продаже')
    subscribe_films = Film.objects.filter(subscribe=True)
    context = {'form': SignupForm(), 'week_films': week_films, 'soon_films': soon_films, 'subscribe_films': subscribe_films, 'modal': modal}
    return render(request, 'films/index.html', context)

def contact(request):
    modal = check_modal(request)
    context = {'form': SignupForm(), 'modal': modal}
    return render(request, 'films/contact.html', context)

def help(request):
    modal = check_modal(request)
    question_list = Question.objects.all()
    context = {'form': SignupForm(), 'question_list': question_list, 'modal': modal}
    return render(request, 'films/help.html', context)

def film_list(request):
    modal = check_modal(request)
    genres = get_genres()
    films = Film.objects.filter(subscribe=False)
    context = {'form': SignupForm, 'films': films, 'genres': genres, 'modal': modal}
    return render(request, 'films/film_list.html', context)

def film_library(request):
    modal = check_modal(request)
    genres = get_genres()
    films = Film.objects.filter(subscribe=True)
    context = {'form': SignupForm, 'films': films, 'genres': genres, 'modal': modal}
    return render(request, 'films/film_library.html', context)

def full_page_week(request):
    modal = check_modal(request)
    genres = get_genres()
    films = Film.objects.filter(subscribe=False)
    films_with_session = Film.objects.annotate(sessions_count=Count("sessions")).filter(sessions_count__gt=0)

    start_date = datetime.now()
    end_date = datetime.now() + timedelta(days=7)
    week_films = []
    for film in films_with_session:
        first_session = film.sessions.order_by('time').last()
        if start_date < first_session.time < end_date:
            week_films.append(film)
    context = {'form': SignupForm, 'films': week_films, 'genres': genres, 'modal': modal}
    return render(request, 'films/film_list.html', context)

def full_page_soon(request):
    modal = check_modal(request)
    genres = get_genres()
    soon_films = Film.objects.filter(subscribe=False).filter(tag='В продаже')
    context = {'form': SignupForm, 'films': soon_films, 'genres': genres, 'modal': modal}
    return render(request, 'films/film_list.html', context)
    
def filter_data(request):
    modal = check_modal(request)
    category = request.POST.get('category')
    genre = request.POST.get('genre')
    text = request.POST.get('text')
    all = request.POST.get('all')
    films = Film.objects.filter(subscribe=False)
    if category != 'None':
        films = films.filter(tag=category)
    if genre != 'None':
        films = films.filter(genres__genre=genre)
    if text != '':
        films = films.filter(title__icontains=text)
    if all:
        films = Film.objects.filter(subscribe=False)
    t = render_to_string('films/filtered_list.html', {'data': films, 'category': category, 'genre': genre, 'text': text, 'modal': modal})
    return JsonResponse({'data': t})

def cinema_list(request):
    modal = check_modal(request)
    cinema_list = Cinema.objects.all()
    context = {'form': SignupForm, 'cinema_list': cinema_list, 'modal': modal}
    return render(request, 'films/cinema_list.html', context)

def buy_ticket(request):
    modal = check_modal(request)
    seats = request.POST.getlist('seats')
    session_id = request.POST.get('session_id')
    customer = request.user
    session = Session.objects.get(pk=session_id)
    for seat in seats:
        session.place_list[str(seat)] = True
        session.save()
        ticket = Ticket(customer=customer, session=session, seat_number=int(seat), price=session.price)
        ticket.save()
    context = {'form': SignupForm, 'seats': seats, 'user': request.user, 'session': session, 'modal': modal}
    return HttpResponseRedirect(reverse('index'))

def history(request):
    ticket_list = Ticket.objects.filter(customer=request.user)
    modal = check_modal(request)
    context = {'form': SignupForm, 'ticket_list': ticket_list, 'modal': modal}
    return render(request, 'films/history.html', context)