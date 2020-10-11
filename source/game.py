from source.player import Player


class Game:

    def __init__(self):
        self.player1 = Player(username='player1')
        self.player2 = Player(username='player2')

    def start_game(self):
        self.player1.serve_ball()
        self.check_game_state()

    def check_game_state(self):
        if self.player1.score == 40 and self.player2.score < 40:
            self.player1.score = 0
            self.player2.score = 0
            self.player1.games_won += 1
