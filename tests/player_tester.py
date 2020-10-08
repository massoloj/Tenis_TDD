import unittest

from unittest.mock import Mock
from source.player import Player


class PlayerTester(unittest.TestCase):

    def setUp(self):
        self.player1 = Player(username='player1')

    def test_serve_ball_scores_a_point(self):
        self.player1._ball_is_hitted_back = Mock(return_value=False)
        self.player1.serve_ball()

        assert self.player1.score == 15

    def test_serve_ball_does_not_score_a_point(self):
        self.player1._ball_is_hitted_back = Mock(return_value=True)
        self.player1.serve_ball()

        assert self.player1.score == 0

if __name__ == '__main__':
    unittest.main()