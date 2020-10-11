import unittest

from unittest.mock import Mock
from source.player import Player
from source.game import Game

class GameTester(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_player_wins_a_game(self):
        self.game.player1.__ball_is_hitted_back = Mock(return_value=False)
        self.game.player1.score = 30

        self.game.start_game()

        assert self.game.player1.score == 0
        assert self.game.player1.games_won == 1

if __name__ == '__main__':
    unittest.main()