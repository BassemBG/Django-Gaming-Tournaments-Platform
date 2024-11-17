from django.contrib import admin
from .models import participation

@admin.register(participation)
class participationAdmin(admin.ModelAdmin):
    list_display = ['participant', 'tournament', 'team_name']
    
    # Fields by which the admin can filter the participations
    list_filter = ('participant', 'tournament', 'team_name')
    
    # Fields by which the admin can sort the participations
    ordering = ('participant', 'tournament', 'team_name')
    
    # Number of participations per page
    list_per_page = 25

# Register your models here.
