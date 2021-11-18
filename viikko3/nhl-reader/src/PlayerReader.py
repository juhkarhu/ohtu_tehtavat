import requests
from player import Player


class PlayerReader:
  def __init__(self, url):
    self.url = url
    

  def get_players(self, nationality):
    response = requests.get(self.url).json()
    result = filter(lambda player: player['nationality'] == nationality, response)

    players = []

    for entry in result:
      player = Player(
        entry['name'],
        entry['nationality'],
        entry['assists'],
        entry['goals'],
        entry['penalties'],
        entry['team'],
        entry['games']
      )
      players.append(player)

    return players