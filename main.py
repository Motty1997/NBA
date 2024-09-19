from flask import Flask

from controllers.player_controller import players_blueprint
from repository.database import create_tables
from utils.load_json import read_players_from_json


app = Flask(__name__)

if __name__ == '__main__':
    create_tables()
    read_players_from_json("./assets/data.json")
    app.register_blueprint(players_blueprint, url_prefix="/api/players")
    app.run(debug=True)