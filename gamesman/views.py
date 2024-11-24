from django.shortcuts import render
from django.http import JsonResponse
from .models import Game
from collections import Counter
from django.db.models import Count

def Games_list(request):
    # Get the sorting parameters from the URL
    sort_order = request.GET.get('sort', '')  # Default is empty (no sorting)
    platform_filter = request.GET.get('platform', '')
    publisher_filter = request.GET.get('publisher', '')  # Filter by publisher
    developer_filter = request.GET.get('developer', '')  # Filter by developer

    # Fetch all game records
    games = Game.objects.all()

    # Apply filters if provided
    if platform_filter:
        games = games.filter(Platform=platform_filter)
    if publisher_filter:
        games = games.filter(Publisher=publisher_filter)
    if developer_filter:
        games = games.filter(Developer=developer_filter)  # Apply developer filter

    # Apply sorting based on the sort parameter
    if sort_order == 'players_asc':
        games = games.order_by('Nb_Players')  # Sort in ascending order by number of players
    elif sort_order == 'players_desc':
        games = games.order_by('-Nb_Players')  # Sort in descending order by number of players

    # Calculate the number of games by Genre using Count and annotate
    genre_counts = Game.objects.values('Genre').annotate(count=Count('Genre')).order_by('-count')

    # Check if the request is AJAX (by looking for the X-Requested-With header)
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        data = [
            {
                'Game_Title': game.Game_Title,
                'Genre': game.Genre,
                'Platform': game.Platform,
                'Release_Date': game.Release_Date.strftime('%Y-%m-%d'),
                'Developer': game.Developer,
                'Publisher': game.Publisher,
                'Nb_Players': game.Nb_Players,
                'File_Size': game.File_Size,
            }
            for game in games
        ]
        return JsonResponse({'games': data})

    # For non-AJAX requests, render the normal page
    return render(request, 'coreApp/games.html', {'games': games, 'genre_counts': genre_counts})

def search_games(request):
    query = request.GET.get('q', '')  # Get the search query
    sort = request.GET.get('sort', '')  # Get the sort parameter from the request
    platform_filter = request.GET.get('platform', '')  # Get platform filter
    publisher_filter = request.GET.get('publisher', '')  # Get publisher filter
    developer_filter = request.GET.get('developer', '')  # Get developer filter

    games = Game.objects.all()

    if query:
        games = games.filter(Game_Title__icontains=query)

    # Apply filters if provided
    if platform_filter:
        games = games.filter(Platform=platform_filter)
    if publisher_filter:
        games = games.filter(Publisher=publisher_filter)
    if developer_filter:
        games = games.filter(Developer=developer_filter)

    # Apply sorting if the sort parameter is provided
    if sort == 'players_asc':
        games = games.order_by('Nb_Players')
    elif sort == 'players_desc':
        games = games.order_by('-Nb_Players')

    data = [
        {'Game_Title': game.Game_Title, 'Genre': game.Genre, 'Platform': game.Platform,
         'Release_Date': game.Release_Date, 'Developer': game.Developer,
         'Publisher': game.Publisher, 'Nb_Players': game.Nb_Players, 'File_Size': game.File_Size}
        for game in games
    ]
    return JsonResponse({'games': data})

def sort_games(request):
    sort_order = request.GET.get('sort', '')  # Get the sort parameter
    games = Game.objects.all()

    # Apply sorting based on the sort parameter
    if sort_order == 'players_asc':
        games = games.order_by('Nb_Players')
    elif sort_order == 'players_desc':
        games = games.order_by('-Nb_Players')

    # Serialize the game data
    data = [
        {
            'Game_Title': game.Game_Title,
            'Genre': game.Genre,
            'Platform': game.Platform,
            'Release_Date': game.Release_Date.strftime('%Y-%m-%d'),
            'Developer': game.Developer,
            'Publisher': game.Publisher,
            'Nb_Players': game.Nb_Players,
            'File_Size': game.File_Size,
        }
        for game in games
    ]
    return JsonResponse({'games': data})

def get_filtered_games(request):
    """Handle dynamic filtering of games based on platform, publisher, and developer."""    
    platform_filter = request.GET.get('platform', '')  # Get platform filter from request
    publisher_filter = request.GET.get('publisher', '')  # Get publisher filter from request
    developer_filter = request.GET.get('developer', '')  # Get developer filter from request

    # Fetch all game records
    games = Game.objects.all()

    # Apply filters if provided
    if platform_filter:
        games = games.filter(Platform=platform_filter)
    if publisher_filter:
        games = games.filter(Publisher=publisher_filter)
    if developer_filter:
        games = games.filter(Developer=developer_filter)  # Apply developer filter

    # Serialize the filtered games to send as JSON response
    data = [
        {
            'Game_Title': game.Game_Title,
            'Genre': game.Genre,
            'Platform': game.Platform,
            'Release_Date': game.Release_Date.strftime('%Y-%m-%d'),
            'Developer': game.Developer,
            'Publisher': game.Publisher,
            'Nb_Players': game.Nb_Players,
            'File_Size': game.File_Size,
        }
        for game in games
    ]
    return JsonResponse({'games': data})

def get_genre_statistics(games):
    """Calculate and return the genre statistics for the given games."""
    # Count games by Genre using the Counter module
    genre_count = Counter(game.Genre for game in games)

    # Ensure the counts are integers
    genre_count = {genre: int(count) for genre, count in genre_count.items()}

    return genre_count