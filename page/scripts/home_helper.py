import json
import calendar
import requests

# accepts json and returns relevant data in list
def format_games_json(games_list_in, team_id):
    games_list = json.loads(games_list_in)

    data = {}

    test = "games_list"

    data["year"] = games_list["data"][0]["date"][0:4]
    data["month"] = calendar.month_name[int(games_list["data"][0]["date"][5:7])]
    data["day"] = games_list["data"][0]["date"][8:10]

    data["home"] = games_list["data"][0]["home_team"]["name"]
    data["away"] = games_list["data"][0]["visitor_team"]["name"]

    data["home_score"] = games_list["data"][0]["home_team_score"]
    data["away_score"] = games_list["data"][0]["visitor_team_score"]

    data["win_score"] = max(games_list["data"][0]["home_team_score"], games_list["data"][0]["visitor_team_score"])
    data["lose_score"] = min(games_list["data"][0]["home_team_score"], games_list["data"][0]["visitor_team_score"])

    data["postseason"] = bool(games_list["data"][0]["postseason"])

    if games_list["data"][0]["home_team_score"] > games_list["data"][0]["visitor_team_score"]:
        data["winner"] = data["home"]
    else:
        data["winner"] = data["away"]

    if team_id == games_list["data"][0]["id"]:
        data["team_is_home"] = True
    else:
        data["team_is_home"] = False
    
    return data


def init_player_list(user):
    players = [get_full_name(user.player1), get_full_name(user.player2), get_full_name(user.player3)]
    return players


def get_full_name(player):
    return player.first_name + " " + player.last_name

def get_player_stats(team_in):

    url = "https://api-nba-v1.p.rapidapi.com/games"

    querystring = {"team":team_in.team_id, "season":"2021", "league":"standard"}

    headers = {
        "X-RapidAPI-Key": "c96660af5dmsh0be727ff1538a07p13726ajsn551e28f3fd42",
        "X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    #getting most recent game_id for user team
    length = len(response["response"])
    x = 1

    #ignoring games that don't exist (ex. playoff games that didn't happen due to series ending before 7 games)
    while response["response"][length - x]["scores"]["home"]["points"] == None:
        x += 1

    game_id = response["response"][length - x]["id"]

    url = "https://api-nba-v1.p.rapidapi.com/players/statistics"

    querystring = {"game":game_id}

    headers = {
        "X-RapidAPI-Key": "c96660af5dmsh0be727ff1538a07p13726ajsn551e28f3fd42",
        "X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    player_stats = {}

    for player in response["response"]:
        if player["team"]["id"] == team_in.team_id:
            player_stats[player["player"]["id"]] = [player["min"], player["points"]]

    return player_stats
