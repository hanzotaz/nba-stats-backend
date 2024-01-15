from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.static import players

class NBAPlayerAPI:
    def __init__(self):
        self.nba_players = players.get_players()

    def get_carreer_data(self, player_name):
        try:
            player_id = [
                player for player in self.nba_players if player["full_name"] == player_name
            ][0]["id"]

            career = playercareerstats.PlayerCareerStats(player_id=player_id)
            return career.get_json()
        except IndexError:
            return {"error": "Player not found"}