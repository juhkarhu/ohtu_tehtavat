from PlayerReader import PlayerReader
from datetime import datetime


class PlayerStats():

  def __init__(self, reader):
    self.reader = reader

  """Get players from certain nationality and sorts them based on goals+assists."""
  def top_scorers_by_nationality(self, nationality):
    response = self.reader.get_players(nationality)

    response.sort(key=lambda player: player.goals + player.assists, reverse=True) 

    print(f'Player from {nationality}', datetime.now())

    return response

