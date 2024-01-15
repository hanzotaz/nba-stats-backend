from flask import Flask, request
from app.players_api import NBAPlayerAPI
from app.teams_api import NBATeamAPI

app = Flask(__name__)

team_service = NBATeamAPI()
player_service = NBAPlayerAPI()

@app.route('/teams', methods=['GET'])
def teams_process():
    team_name = request.get_json().get('team', '')
    result = team_service.get_teams_data(team_name)

    return result

@app.route('/players', methods=['GET'])
def players_process():
    player_name = request.get_json().get('name', '')
    result = player_service.get_carreer_data(player_name)

    return result