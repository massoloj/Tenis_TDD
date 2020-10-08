from asyncio import wait
from random import random

from source.constants import POINT


class Player:

    def __init__(self, username):
        self.username = username
        self.score = 0

    @classmethod
    def _ball_is_hitted_back(cls):
        return bool(random.getrandbits(1))

    def serve_ball(self):
        print(f'Player {self.username} served the ball')
        

        if self._ball_is_hitted_back():
            print(f'The ball was returned by the other player')
        else:
            print(f'Player {self.username} scored a point')
            self.score += POINT

    def return_ball(self):
        ball_is_hitted_back = random.choice([True, False])

        if ball_is_hitted_back:
            #call receive method
            pass
        else:
            #call end_current_game method
            pass
