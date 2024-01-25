import json
from datetime import timezone
from dateutil import parser
from nba_api.live.nba.endpoints import scoreboard


class NBALivesScoreBoard:
    def __init__(self):
        self.score = scoreboard.ScoreBoard()

    def get_all_scoreboards(self):
        try:
            games = self.score.games.get_dict()
            scoreboardDict = {"date": self.score.score_board_date, "games": {}}

            for game in games:
                gameTimeLTZ = (
                    parser.parse(game["gameTimeUTC"])
                    .replace(tzinfo=timezone.utc)
                    .astimezone(tz=None)
                )

                game_info = {
                    "gameTimeLTZ": gameTimeLTZ.isoformat(),
                    "homeTeam": game["homeTeam"]["teamName"],
                    "homeScore": game["homeTeam"]["score"],
                    "awayTeam": game["awayTeam"]["teamName"],
                    "awayScore": game["awayTeam"]["score"],
                }

                scoreboardDict["games"][game["gameId"]] = game_info
            return json.dumps(scoreboardDict)
        except Exception as e:
            return {"error": f"Error retrieving live scoreboards: {str(e)}"}
