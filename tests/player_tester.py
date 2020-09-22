import unittest

from source.constants import POINT


class PlayerTester(unittest.TestCase):

    def setUp(self):
        self.player1 = Player(username='player1')
        self.player2 = Player(username='player2')
        self.game = Game(Player1, Player2)

    def test_serve_success(self):
        player1.serve()
        yield
        assert player1.current_points == POINT
