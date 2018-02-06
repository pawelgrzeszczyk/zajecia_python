from django.contrib import admin

# Register your models here.
from .models import Category, News



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('nazwa', 'ikona')
    prepopulated_fields = {'odnosnik': ('nazwa',)}


class NewsAdmin(admin.ModelAdmin):
    list_display = ('tytul', 'data_publikacji')
    prepopulated_fields = {'odnosnik': ('tytul',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(News, NewsAdmin)