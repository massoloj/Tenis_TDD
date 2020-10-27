import unittest

from unittest.mock import patch
from source.game import Game


class GameTester(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_serve_ball_scores_a_point(self):
        with patch('source.game.Game.ball_is_hitted_back') as mocked_ball:
            mocked_ball.return_value = False
            self.game.move_player(self.game.player1)

            assert self.game.player1.score == 15

    def test_serve_ball_scores_a_game_point(self):
        with patch('source.game.Game.ball_is_hitted_back') as mocked_ball:
            mocked_ball.return_value = False
            self.game.player1.score = 30

            self.game.move_player(self.game.player1)

            assert self.game.player1.score == 40

    def test_serve_ball_does_not_score_a_point(self):
        with patch('source.game.Game.ball_is_hitted_back') as mocked_ball:
            mocked_ball.return_value = True

            self.game.move_player(self.game.player1)

            assert self.game.player1.score == 0

    def test_player_wins_a_game(self):
        with patch('source.game.Game.ball_is_hitted_back') as mocked_ball:
            mocked_ball.return_value = False
            self.game.player1.score = 30

            self.game.move_player(self.game.player1)
            self.game.check_game_state(self.game.player1, self.game.player2)

            assert self.game.player1.score == 0
            assert self.game.player1.games_won == 1

    def test_player_wins_a_set(self):
        with patch('source.game.Game.ball_is_hitted_back') as mocked_ball:
            mocked_ball.return_value = False
            self.game.player1.games_won = 5
            self.game.player1.score = 30

            self.game.move_player(self.game.player1)
            self.game.check_game_state(self.game.player1, self.game.player2)

            assert self.game.player1.score == 0
            assert self.game.player1.games_won == 0
            assert self.game.player1.sets_won == 1

    def test_deuce(self):
        with patch('source.game.Game.ball_is_hitted_back') as mocked_ball:
            mocked_ball.return_value = False
            self.game.player1.score = 30
            self.game.player2.score = 40

            self.game.move_player(self.game.player1)

            assert self.game.player1.score == 40
            assert self.game.player1.games_won == 0

    def test_player_wins_game_after_deuce(self):
        with patch('source.game.Game.ball_is_hitted_back') as mocked_ball:
            mocked_ball.return_value = False
            self.game.player1.score = 40
            self.game.player2.score = 40

            self.game.move_player(self.game.player1)
            self.game.move_player(self.game.player1)
            self.game.check_game_state(self.game.player1, self.game.player2)

            assert self.game.player1.score == 0
            assert self.game.player1.games_won == 1


if __name__ == '__main__':
    unittest.main()
