from asyncio import wait
from random import random

from source.constants import POINT


class Player:

    def __init__(self, username):
        self.username = username
        self.score = 0

    def serve_ball(self):
        self.score += POINT

    def return_ball(self):
        ball_is_hitted_back = random.choice([True, False])

        if ball_is_hitted_back:
            #call receive method
            pass
        else:
            #call end_current_game method
            pass
