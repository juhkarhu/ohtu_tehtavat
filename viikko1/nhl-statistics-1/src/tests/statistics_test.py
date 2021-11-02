import unittest
from statistics import Statistics
from player import Player



class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
  def setUp(self):
    self.statistics = Statistics(PlayerReaderStub())


  def test_returns_list_of_5(self):
    arr = self.statistics._players
    self.assertAlmostEqual(len(arr), 5)

  def test_top_scorer_is_Gretzky(self):
    arr = self.statistics.top_scorers(1)
    self.assertEqual(arr[0].name, 'Gretzky')

  def test_one_player_from_DET(self):
    arr = self.statistics.team('DET')
    self.assertAlmostEqual(len(arr), 1)

  def test_search_for_Lemieux(self):
    player = self.statistics.search('Lemieux')
    self.assertEqual(player.name, 'Lemieux')

  def test_search_for_nonexisting_player(self):
    player = self.statistics.search('Jokinen')
    self.assertEqual(player, None)