import sys
import unittest
from io import StringIO

from source.player import Player


class PlayerTester(unittest.TestCase):

    def setUp(self):
        self.player1 = Player(username='player1')

    def test_serve_ball(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput

        self.player1.serve_ball()
        sys.stdout = sys.__stdout__

        print('value:', capturedOutput.getvalue())
        assert capturedOutput.getvalue() == 'Player player1 served the ball\n'


if __name__ == '__main__':
    unittest.main()
