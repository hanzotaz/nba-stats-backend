from nba_api.live.nba.endpoints import scoreboard

class NBALivesScoreBoard():
    def __init__(self):
        self.games = scoreboard.ScoreBoard()

    def get_all_scoreboards(self):
        try:
            return self.games.get_json()
        except Exception as e:
            return {"error": f"Error retrieving live scoreboards: {str(e)}"}