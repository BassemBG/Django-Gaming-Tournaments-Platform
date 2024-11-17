from django.contrib import admin
from .models import user

@admin.register(user)
class YourModelNameAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'role')