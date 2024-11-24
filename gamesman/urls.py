from django.urls import path
from . import views

urlpatterns = [
    path('Games_list', views.Games_list, name='Games_list'),
    path('search_games/', views.search_games, name='search_games'),  # Search games
    path('sort_games/', views.sort_games, name='sort_games'),  # Sort games
    path('filter_games/', views.get_filtered_games, name='filter_games'), 
    path('genre_statistics/', views.get_genre_statistics, name='genre_statistics'), 
    
      # Combined filter for platform and publisher
]
