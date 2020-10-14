import unittest

from unittest import mock
from unittest.mock import patch

from source.player import Player

class PlayerTester(unittest.TestCase):

    def setUp(self):
        self.player1 = Player(username='player1')

    def test_serve_ball_scores_a_point(self):
        with patch('source.player.Player.ball_is_hitted_back') as mocked_ball:
            mocked_ball.return_value = False
            self.player1.serve_ball()

            assert self.player1.score == 15

    def test_serve_ball_scores_a_game_point(self):
        with patch('source.player.Player.ball_is_hitted_back') as mocked_ball:
            mocked_ball.return_value = False
            self.player1.score = 30
            self.player1.serve_ball()

            assert self.player1.score == 40

    def test_serve_ball_does_not_score_a_point(self):
        with patch('source.player.Player.ball_is_hitted_back') as mocked_ball:
            mocked_ball.return_value = True
            self.player1.serve_ball()

            assert self.player1.score == 0


if __name__ == '__main__':
    unittest.main()
