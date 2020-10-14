import unittest

from unittest.mock import Mock, patch
from source.player import Player
from source.game import Game

class GameTester(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_player_wins_a_game(self):
        with patch('source.player.Player.ball_is_hitted_back') as mocked_ball:
            mocked_ball.return_value = False
            self.game.player1.score = 30

            self.game.start_game()

            assert self.game.player1.score == 0
            assert self.game.player1.games_won == 1


if __name__ == '__main__':
    unittest.main()