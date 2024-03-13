from django.contrib import admin

# Register your models here.

from django.contrib import admin

from users.models import User


@admin.register(User)
class CategoryAdmin(admin.ModelAdmin):
    pass