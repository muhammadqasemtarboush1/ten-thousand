from random import *

class GameLogic:
    def __init__(self):
        pass

    def roll_dice(num_dice):
            return tuple(randint(1, num_dice) for num in range(num_dice))

    def calculate_score(self):
        pass
