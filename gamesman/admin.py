# gamesman/admin.py
from django.contrib import admin
from .models import Game

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('Game_Title', 'Genre', 'Platform', 'Release_Date', 'Developer', 'Publisher', 'Nb_Players', 'File_Size')
    search_fields = ('Game_Title', 'Developer', 'Publisher')
    list_filter = ('Platform', 'Genre', 'Release_Date')


