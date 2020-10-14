import random

from source.constants import POINT, GAME_POINT


class Player:

    def __init__(self, username):
        self.username = username
        self.score = 0
        self.games_won = 0

    def ball_is_hitted_back(self):
        return bool(random.getrandbits(1))

    def serve_ball(self):
        print(f'Player {self.username} served the ball')

        if self.ball_is_hitted_back():
            print(f'The ball was returned by the other player')
        else:
            if self.score == 30:
                print(f'Player {self.username} scored a game point')
                self.score += GAME_POINT
            else:
                print(f'Player {self.username} scored a point')
                self.score += POINT
