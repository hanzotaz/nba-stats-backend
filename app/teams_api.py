from flask import jsonify

from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder

class NBATeamAPI:
    def __init__(self):
        self.nba_teams = teams.get_teams()
        
    def get_teams_data(self, team_name):
        try:
            team = [
                team for team in self.nba_teams if team["full_name"] == team_name
            ][0]

            return jsonify(team)
        except IndexError:
            return {"error": "Team not found"}
        
    def get_teams_game(self, team_name):
        try:
            team_id = [
               team for team in self.nba_teams if team["full_name"] == team_name
            ][0]["id"]

            gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=team_id)
            return gamefinder.get_json()
        
        except IndexError:
            return {"error": "Team not found"}