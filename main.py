from api.players_api import NBAPlayerAPI

def main():
    # Initialize Player API
    player_api_instance = NBAPlayerAPI()

    try:
        # Run the Player API
        player_api_instance.run()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()