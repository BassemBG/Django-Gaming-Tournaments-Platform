from django.contrib import admin
from django.db.models import Count, Sum
from django.urls import path
from django.shortcuts import render
from django.utils.html import format_html
from .models import Game


class GameAdmin(admin.ModelAdmin):
    list_display = (
        'Game_Title', 'Genre', 'Platform',
        'Release_Date', 'Developer', 'Publisher',
        'Nb_Players', 'File_Size', 'dashboard_button'
    )
    search_fields = ('Game_Title', 'Developer', 'Publisher')
    list_filter = ('Platform', 'Genre', 'Release_Date')
    ordering = ('-Nb_Players',)

    # Add a button for viewing the dashboard
    def dashboard_button(self, obj):
        return format_html(
            '<a class="button" href="{}">View Dashboard</a>',
            '/admin/gamesman/game/dashboard/'  # Link to the dashboard
        )
    dashboard_button.short_description = "Dashboard"

    def get_urls(self):
        # Default admin URLs
        urls = super().get_urls()
        # Custom URL for the dashboard
        custom_urls = [
            path('dashboard/', self.dashboard_view, name='game_dashboard'),
        ]
        return custom_urls + urls

    def dashboard_view(self, request):
        # Calculate data for the dashboard
        genre_counts = Game.objects.values('Genre').annotate(count=Count('Genre')).order_by('-count')
        platform_counts = Game.objects.values('Platform').annotate(count=Count('Platform')).order_by('-count')
        developer_counts = Game.objects.values('Developer').annotate(count=Count('Developer')).order_by('-count')

        total_games = Game.objects.count()
        total_players = Game.objects.aggregate(Sum('Nb_Players'))['Nb_Players__sum'] or 0

        # Prepare data for rendering
        context = {
            'total_games': total_games,
            'total_players': total_players,

            # Data for charts
            'genres': [item['Genre'] for item in genre_counts],
            'genre_counts': [item['count'] for item in genre_counts],
            'platforms': [item['Platform'] for item in platform_counts],
            'platform_counts': [item['count'] for item in platform_counts],
            'developers': [item['Developer'] for item in developer_counts],
            'developer_counts': [item['count'] for item in developer_counts],
        }
 
        # Render the statistics template
        return render(request, 'admin/statistics.html', context)


# Register the Game model with the custom admin
admin.site.register(Game, GameAdmin)
