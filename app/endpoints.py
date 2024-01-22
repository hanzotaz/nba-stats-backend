from flask import Flask, request
from flask_cors import CORS
from flask_socketio import SocketIO
from app.players_api import NBAPlayerAPI
from app.teams_api import NBATeamAPI
from app.scoreboard_api import NBALivesScoreBoard

app = Flask(__name__)
CORS(app)
socket = SocketIO(app)

team_service = NBATeamAPI()
player_service = NBAPlayerAPI()
live_game_service = NBALivesScoreBoard()


@app.route("/teams", methods=["GET"])
def teams_process():
    team_name = request.args.get("team", "")

    if "true" in request.args.get("game", "").lower():
        result = team_service.get_teams_game(team_name)
    else:
        result = team_service.get_teams_data(team_name)

    return result


@app.route("/players", methods=["GET"])
def players_process():
    player_name = request.args.get("name", "")
    result = player_service.get_carreer_data(player_name)

    return result


@app.route("/live", methods=["GET"])
def live_games_process():
    result = live_game_service.get_all_scoreboards()

    return result


@socket.on("connect")
def handle_connect():
    client_ip = request.remote_addr
    print(f"Client [{client_ip}] connected")


@socket.on("disconnect")
def handle_disconnect():
    client_ip = request.remote_addr
    print(f"Client [{client_ip}] disconnected")


def emit_live_scoreboard():
    while True:
        live_scores = live_game_service.get_all_scoreboards()
        socket.emit("live_score_update", live_scores)
        socket.sleep(10)


def run_flask():
    socket.run(app, port=5001, use_reloader=False, log_output=False)


if __name__ == "__main__":
    socket.start_background_task(emit_live_scoreboard)
    run_flask()
