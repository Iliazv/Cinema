from django.contrib import admin
from .models import Film, Session, Genre, Image, User, Question, Cinema, Ticket
from django.utils.html import format_html

#kinoman112

if not hasattr(admin, "display"):
    def display(description):
        def decorator(fn):
            fn.short_description = description
            return fn
        return decorator
    setattr(admin, "display", display)

class AdminModel(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    list_display = ['email', 'is_superuser']
    search_fields = ['email']

class ImageInline(admin.StackedInline):
    model = Image
    extra = 3

class FilmAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    search_fields = ['title', 'country', 'subscribe']

class CinemaAdmin(admin.ModelAdmin):
    list_display = ['name', 'location']
    search_fields = ['name']

class SessionAdmin(admin.ModelAdmin):
    search_fields = ['film__title', 'time']
    autocomplete_fields = ['film', 'cinema']
    list_display = ['get_film_name', 'time']

    @admin.display(description='Фильм')
    def get_film_name(self,obj):
        return obj.film.title
    
class GenreAdmin(admin.ModelAdmin):
    search_fields = ['film__title', 'genre']
    autocomplete_fields = ['film']
    list_display = ['get_film_name', 'genre']

    @admin.display(description='Фильм')
    def get_film_name(self,obj):
        return obj.film.title

class TicketAdmin(admin.ModelAdmin):
    search_fields = ['customer', 'session']
    list_display = ['customer', 'session']

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['notation']
    list_display = ['notation', 'slice']

    @admin.display(description='Вопрос')
    def slice(self, obj):
        if len(obj.text) >= 77:
            return f'{obj.text[:77]}...'
        return obj.text[:80]


admin.site.register(User, AdminModel)
admin.site.register(Film, FilmAdmin)
admin.site.register(Cinema, CinemaAdmin)
admin.site.register(Session, SessionAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Question, QuestionAdmin)
