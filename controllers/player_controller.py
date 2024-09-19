from dataclasses import asdict
from flask import Blueprint, jsonify, request
from repository.players_repository import find_all_players


players_blueprint = Blueprint("players", __name__)

@players_blueprint.route("/", methods=['GET'])
def get_all():
    req_data = request.args.to_dict()
    players = list(map(asdict, find_all_players()))
    return jsonify(players), 200
