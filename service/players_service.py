from toolz import *
from repository.database import create_tables
from repository.players_repository import create_player, find_all_players
from utils.load_json import read_players_from_json
from models.player import Player
from service.ppg_ratio_func import ppg_ratio


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
                                  x["assists"],
                                  x["turnovers"],
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
    for player in _players:
        create_player(player)

all_players = find_all_players()
if len(all_players) <= 0:
    create_players_in_db(players)

one = Player('Aaron Gordon', 'PF', 75, 0.335, 0.605, 0.573, 188, 133, 1126, 'DEN', 2022, 'gordoaa01')
c = ppg_ratio(one ,all_players)
print(c)
