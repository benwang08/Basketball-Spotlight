from django.shortcuts import render
import requests
from datetime import datetime, timedelta
from .models import User, Player, Team
from.scripts import home_helper, database_helper

import json;

def home(request):

    #gets user object from database for current logged in user
    user = request.user

    #update team roster of user's team
    # database_helper.populate_roster(user.team)

        
    #getting start_date, yesterdays date

    yesterday = datetime.now() - timedelta(1)
    yesterday_date = yesterday.isoformat()[0:10]
    yesterday_date = "2020-02-10"
    #queries for games, general games (yesterdays) and user specific (based on followed team)
    post_for_pages = requests.get(f'https://www.balldontlie.io/api/v1/games?start_date={yesterday_date}&end_date={yesterday_date}&per_page=1').json()

    num_pages = post_for_pages["meta"]["total_pages"]
    query_range = 4
    if num_pages < 4:
        query_range = num_pages

    general_game_data = []

    #get last 4 games
    for i in range(query_range):
        num_pages = num_pages - i
        general_game_data.append(requests.get(f'https://www.balldontlie.io/api/v1/games?start_date={yesterday_date}&end_date={yesterday_date}&per_page=1&page={num_pages}').json())

    #get last game of users followed team
    post_for_pages = requests.get(f'https://www.balldontlie.io/api/v1/games?team_ids[]={str(user.team_id)}&per_page=1').json()

    num_pages = post_for_pages["meta"]["total_pages"]

    user_game_data = requests.get(f'https://www.balldontlie.io/api/v1/games?team_ids[]={str(user.team_id)}&per_page=1&page={num_pages}').json()


    general_games = []
    for i in range(query_range):
        general_games.append(home_helper.format_games_json(json.dumps(general_game_data[i]), user.team_id))


    user_game = home_helper.format_games_json(json.dumps(user_game_data), user.team_id)

    #data for player section
    player_stats_temp = home_helper.get_player_stats(user.team)

    for roster_player in Player.objects.get(team = user.team):
        if player_stats_temp.get(roster_player.npa_api_id) == None:
            player_stats_temp[roster_player.npa_api_id] = ["0:00", "0"]
    
    player_stats = {}
    for key, value in player_stats_temp:
        player_stats[Player.objects.get(nba_api_id = key)] = value


    content = {
        'title': 'home',
        'current_user': user,
        'general_game_data': general_games,
        'user_game_data': user_game,
        'player_stats' : player_stats,
        'range' : range(4)
    }

    return render(request, 'page/home.html', content)

def about(request):
    return render(request, 'page/about.html', {'title' : 'about'})

def login(request):
    return render(request, 'page/login.html')

