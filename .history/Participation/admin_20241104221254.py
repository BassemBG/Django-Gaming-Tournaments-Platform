from django.contrib import admin
from .models import participation

@admin.register(participation)
class participationAdmin(admin.ModelAdmin):
    list_display = ['participant', 'tournament', 'team_name']
# Register your models here.
