from django.contrib import admin

from .models import Autor, Wydawnictwo, Book
# Register your models here.

class AutorAdmin(admin.ModelAdmin):
    search_fields = ['imie', 'nazwisko']
    ordering = ['imie']

class WydawnictwoAdmin(admin.ModelAdmin):
    search_fields = ['nazwa']
    ordering = ['nazwa']

class BookAdmin(admin.ModelAdmin):
    search_fields = ['tytul']
    list_display = ['tytul', 'autor', 'wydawnictwo']

admin.site.register(Autor, AutorAdmin)
admin.site.register(Wydawnictwo, WydawnictwoAdmin)
admin.site.register(Book, BookAdmin)