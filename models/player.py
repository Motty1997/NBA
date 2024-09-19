from dataclasses import dataclass

@dataclass
class Player:
   player_name: str
   position: str
   games: int
   three_percent: float
   two_percent: float
   effective_fg_percent: float
   atr: float
   points: int
   team: str
   season: int
   player_id: str
