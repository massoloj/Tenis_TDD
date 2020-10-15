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
            print('In condition 1')
            self.player1.score = 0
            self.player2.score = 0
            if self.player1.games_won == 5:
                self.player1.sets_won += 1
                self.player1.games_won = 0
                self.player2.games_won = 0
            else:
                self.player1.games_won += 1

        if self.player1.score > 40 and (self.player1.score - self.player2.score > 10):
            print('In condition 2')
            print('Score player 1: ', self.player1.score)
            print('Score player 2: ', self.player2.score)
            self.player1.score = 0
            self.player2.score = 0
            self.player1.games_won += 1

        print('No conditions match')
