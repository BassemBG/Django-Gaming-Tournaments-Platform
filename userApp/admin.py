from django.contrib import admin
from .models import user

@admin.register(user)
class userAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'role')