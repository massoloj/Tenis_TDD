import unittest

from source.player import Player


class PlayerTester(unittest.TestCase):

    def setUp(self):
        self.player1 = Player(username='player1')

    def test_serve_ball_success(self):
        self.player1.serve_ball()

        assert self.player1.score == 15


if __name__ == '__main__':
    unittest.main()