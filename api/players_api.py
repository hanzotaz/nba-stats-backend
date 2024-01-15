from flask import Flask, request

from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.static import players

class NBAPlayerAPI:
    def __init__(self):
        self.app = Flask(__name__)
        self.nba_players = players.get_players()

        @self.app.route('/players', methods=['POST'])
        def process():
            player_name = request.get_json().get('name', '')
            result = self.get_players_data(player_name)
            return result

    def get_players_data(self, player_name):
        player_id = [
            player for player in self.nba_players if player["full_name"] == player_name
        ][0]["id"]

        career = playercareerstats.PlayerCareerStats(player_id=player_id)
        return career.get_json()

    def run(self):
        self.app.run(debug=True)

if __name__ == '__main__':
    nba_player_api = NBAPlayerAPI()
    nba_player_api.run()