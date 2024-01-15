from flask import jsonify

from nba_api.stats.static import teams

class NBATeamAPI:
    def __init__(self):
        self.nba_teams = teams.get_teams()
        
    def get_teams_data(self, team_name):
        team = [
            team for team in self.nba_teams if team["full_name"] == team_name
        ][0]

        return jsonify(team)