from django.contrib import admin
from .models import user

@admin.register(Participant)
class YourModelNameAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'role')