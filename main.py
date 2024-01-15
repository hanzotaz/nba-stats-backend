from api.teams_api import NBATeamAPI
from api.players_api import NBAPlayerAPI

if __name__ == '__main__':
    nba_team_api = NBATeamAPI()
    nba_player_api = NBAPlayerAPI()

    nba_team_api.run()
    nba_player_api.run()