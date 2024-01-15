from threading import Thread
from app.endpoints import run_flask

def main():
    # Create separate threads for Flask endpoints
    flask_thread = Thread(target=run_flask)

    # Start the threads
    flask_thread.start()

    # Wait for threads to finish
    flask_thread.join()

if __name__ == '__main__':
    main()