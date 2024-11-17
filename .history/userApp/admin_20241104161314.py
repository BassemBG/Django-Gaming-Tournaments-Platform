from django.contrib import admin
from .models import Participant

@admin.register(Participant)
class YourModelNameAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'role')