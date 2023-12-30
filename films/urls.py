from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('film/<int:pk>', views.film_page, name='film_page'),
    path('cinema/<slug:slug>', views.cinema_page, name='cinema_page'),
    path('register/', views.register, name='register'),
    path('registered/', views.registered, name='registered'),
    path('login/', views.login, name='login'),
    path('logout_view/', views.logout_view, name='logout_view'),
    path('contact/', views.contact, name='contact'),
    path('help/', views.help, name='help'),
    path('film_list/', views.film_list, name='film_list'),
    path('film_library/', views.film_library, name='film_library'),
    path('full_page_week/', views.full_page_week, name='full_page_week'),
    path('full_page_soon/', views.full_page_soon, name='full_page_soon'),
    path('filter_data/', views.filter_data, name='filter_data'),
    path('cinema_list/', views.cinema_list, name='cinema_list'),
    path('buy_ticket/', views.buy_ticket, name='buy_ticket'),
    path('history/', views.history, name='history'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)