from toolz import *
from repository.database import create_tables
from repository.players_repository import create_player, find_all_players
from utils.load_json import read_players_from_json
from models.player import Player
from service.ppg_ratio_and_art_func import ppg_ratio
from service.ppg_ratio_and_art_func import atr_calculator


list_players_from_api = read_players_from_json("../assets/data.json")

def list_players(trivia_from_api):
    return pipe(
        trivia_from_api,
        lambda li: map(lambda x: Player(x["playerName"],
                                  x["position"],
                                  x["games"],
                                  x["threePercent"],
                                  x["twoPercent"],
                                  x["effectFgPercent"],
                                  atr_calculator(x["assists"], x["turnovers"]),
                                  x["points"],
                                  x["team"],
                                  x["season"],
                                  x["playerId"]
                                        ), li),
        list,
    )

players = list_players(list_players_from_api)

def create_players_in_db(_players):
    create_tables()
    if len(find_all_players()) <= 0:
        for player in _players:
            create_player(player)

create_players_in_db(players)
