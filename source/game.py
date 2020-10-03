from source.ball import Ball
from source.player import Player


class Game:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.ball = Ball()

    def start_game(self):
        self.player1.serve_ball()
        self.player1.serve_ball()
