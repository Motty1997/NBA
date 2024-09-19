from models.player import Player
from repository.database import get_db_connection
from typing import List


def create_player(player: Player) -> str:
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("""
        INSERT INTO players (
                    player_name,
                    position,
                    games,
                    three_percent,
                    two_percent,
                    effective_fg_percent,
                    assists,
                    turnovers,
                    points,
                    team,
                    season,
                    player_id
                )
         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """, (player.player_name,
              player.position,
              player.games,
              player.three_percent,
              player.two_percent,
              player.effective_fg_percent,
              player.assists, player.turnovers,
              player.points,
              player.team,
              player.season,
              player.player_id))
        connection.commit()


def find_all_players() -> List[Player]:
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("SELECT * FROM players")
        res = cursor.fetchall()
        players = [Player(**p) for p in res]
        return players
