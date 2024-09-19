from models.player import Player


def atr_calculator(player: Player) -> float:
    atr = player.assists / player.turnovers
    return atr
