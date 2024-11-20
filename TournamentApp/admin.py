from django.contrib import admin
from .models import tournament, TournamentEquipment

# Register the tournament model
@admin.register(tournament)
class TournamentAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'location', 'status', 'prize', 'price', 'team_size', 'game')
    list_filter = ('status', 'game', 'start_date')
    search_fields = ('name', 'location', 'description')

# Register the TournamentEquipment model
@admin.register(TournamentEquipment)
class TournamentEquipmentAdmin(admin.ModelAdmin):
    list_display = ('tournament', 'equipment', 'quantity')
    list_filter = ('tournament', 'equipment')
    search_fields = ('tournament__name', 'equipment__name')