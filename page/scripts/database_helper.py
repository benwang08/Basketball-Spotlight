import json
from typing import OrderedDict
import requests
from ..models import Player, Team

def populate_roster(team_in):
    pages_left = True
    current_page = 1


    url = "https://api-nba-v1.p.rapidapi.com/players"

    querystring = {"team": str(team_in.team_id),"season":"2021"}

    headers = {
        "X-RapidAPI-Key": "c96660af5dmsh0be727ff1538a07p13726ajsn551e28f3fd42",
        "X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    #ordering list of pros by years played to display more senior players first
    ordered_by_pro = list(response["response"])
    ordered_by_pro.sort(key = lambda json : json["nba"]["pro"], reverse=True)

    for i in range(15):
        firstname = ordered_by_pro[i]["firstname"]
        lastname = ordered_by_pro[i]["lastname"]
        api_id = ordered_by_pro[i]["id"]

        #add player with team. If player already exists, player profile will be updated

        person, created = Player.objects.get_or_create(first_name = firstname, last_name = lastname, team = team_in, nba_api_id = api_id)

        if not created:
            person.team = team_in   
            nba_api_id = api_id
