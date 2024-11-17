from django.contrib import admin
from .models import tournament

@admin.register(tournament)
class tournamentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'start_date', 'end_date', 'location', 'status', 'prize', 'price', 'team_size', 'game')
