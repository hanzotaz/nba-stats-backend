from flask import Flask, request, jsonify

from nba_api.stats.static import teams

class NBATeamAPI:
    def __init__(self):
        self.app = Flask(__name__)
        self.nba_teams = teams.get_teams()

        @self.app.route('/teams', methods=['POST'])
        def process():
            team_name = request.get_json().get('team', '')
            result = self.get_teams_data(team_name)
            return result
        
    def get_teams_data(self, team_name):
        team = [
            team for team in self.nba_teams if team["full_name"] == team_name
        ][0]

        return jsonify(team)
    
    def run(self):
        self.app.run(debug=True)

if __name__ == '__main__':
    nba_team_api = NBATeamAPI()
    nba_team_api.run