import unittest
from player import Player
from statistics_service import StatisticsService


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_with_existing_player(self):
        result = self.stats.search("Semenko")

        self.assertEqual(result.name, "Semenko")
        self.assertEqual(result.team, "EDM")
        self.assertEqual(result.goals, 4)
        self.assertEqual(result.assists, 12)

    def test_search_with_nonexisting_player(self):
        result = self.stats.search("Joulupukki")

        self.assertIsNone(result)

    def test_team(self):
        result = self.stats.team("EDM")

        self.assertEqual(len(result), 3)
        self.assertEqual("Semenko", result[0].name)
        self.assertEqual("Kurri", result[1].name)
        self.assertEqual("Gretzky", result[2].name)

    def test_top(self):
        result = self.stats.top(4)

        self.assertEqual(len(result), 5)
        self.assertEqual("Gretzky", result[0].name)
        self.assertEqual("Lemieux", result[1].name)
        self.assertEqual("Yzerman", result[2].name)
        self.assertEqual("Kurri", result[3].name)
        self.assertEqual("Semenko", result[4].name)
