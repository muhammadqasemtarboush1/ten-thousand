from random import *
from collections import Counter


###################
#  Mu'ayad Al Shareef
###################
###################
#  Muhammad Tarboush
###################
class GameLogic:
    def __init__(self):
        pass

    @staticmethod
    def roll_dice(num_dice):
        return tuple(randint(1, num_dice) for num in range(num_dice))

    @staticmethod
    def calculate_score(tuple_of_init):
        base_scores = {1: 1000, 2: 200, 3: 300, 4: 400, 5: 500, 6: 600}
        game_score = 0
        new_tuple = Counter(tuple_of_init)
        high_score = new_tuple.most_common()
        for dice_count in high_score:
            if len(high_score) == 6:
                game_score = 1500
                return game_score
            if len(high_score) == 3 and high_score[0][1] == high_score[1][1] == high_score[2][1] == 2:
                game_score = 1500
                return game_score
            if dice_count[0] == 5 and dice_count[1] <= 2:
                game_score += 50 * dice_count[1]
            if dice_count[0] == 1 and dice_count[1] <= 2:
                game_score += 100 * dice_count[1]
            if dice_count[1] == 3:
                game_score += base_scores[dice_count[0]]
            if dice_count[1] == 4:
                game_score += base_scores[dice_count[0]] * 2
            if dice_count[1] == 5:
                game_score += base_scores[dice_count[0]] * 3
            if dice_count[1] == 6:
                game_score += base_scores[dice_count[0]] * 4
        return game_score

    @staticmethod
    def get_scorers(dice):
        dices_score = GameLogic.calculate_score(dice)
        if dices_score == 0:
            return tuple()
        scorers = []
        for i, value in enumerate(dice):
            slice_rolling = dice[:i] +  dice[i+1 :]
            scoring = GameLogic.calculate_score(slice_rolling)
            if dices_score != scoring:
                scorers.append(value)
        return tuple(scorers)