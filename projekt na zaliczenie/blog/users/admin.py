from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from .models import BlogUser


class BlogUserAdmin(UserAdmin):
    pass

admin.site.register(BlogUser, BlogUserAdmin )