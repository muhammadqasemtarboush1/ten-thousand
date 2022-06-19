try:
    from game_logic import GameLogic
    from banker import Banker
except ImportError:
    from .game_logic import GameLogic
    from .banker import Banker
from collections import Counter

class Game:
    def __init__(self):
        self.round = 1
        self.dice = 6
        self.banker = Banker()

    def play(self, roller=GameLogic.roll_dice):
        cheating_stauts = False
        print('Welcome to Ten Thousand')
        print('(y)es to play or (n)o to decline')
        user_answer = input('> ')
        if user_answer == 'n':
            print('OK. Maybe another time')
            return
        if user_answer == 'y':
            print(f'Starting round {self.round}')
        while True:
            if not cheating_stauts:
                print(f'Rolling {self.dice} dice...')
            new_roller = roller(self.dice)
            formatted_line = "*** " + ' '.join([str(i) for i in new_roller]) + " ***"
            print(formatted_line)
            print('Enter dice to keep, or (q)uit:')
            user_answer = input('> ')
            # check_cheater(user_answer, new_roller)
            cheating_stauts = check_cheater(user_answer, new_roller)
            if user_answer == 'q':
                print(f'Thanks for playing. You earned {self.banker.balance} points')
                return
            if user_answer != 'q':
                if not cheating_stauts:
                    dices = [x for x in user_answer if x.strip() != ""]
                    num_of_dice_shelving = len(dices)
                    dice_kept = map(int, dices)
                    roll_tuple = tuple(dice_kept)
                    score = GameLogic.calculate_score(roll_tuple)
                    self.banker.shelf(score)
                    self.dice -= num_of_dice_shelving

                    print(f'You have {self.banker.shelved} unbanked points and {self.dice} dice remaining')
                    print('(r)oll again, (b)ank your points or (q)uit:')

                    user_choice = input('> ')

                    if user_choice == 'b':
                        print(f'You banked {self.banker.shelved} points in round {self.round}')
                        self.banker.bank()
                        print(f'Total score is {self.banker.balance} points')

                        self.round += 1
                        print(f'Starting round {self.round}')
                        self.dice = 6
                    if user_choice == 'q':
                        print(f'Thanks for playing. You earned {self.banker.balance} points')
                        return


def check_cheater(user_answer, roller):
    dice_values = Counter(roller).most_common()
    user_input = Counter(user_answer).most_common()
    # cheating_stauts = True
    # print(dice_values)
    for i in user_input:
        for j in dice_values:
            if int(i[0]) == j[0] and i[1] <= j[1]:
                return False
    print('Cheater!!! Or possibly made a typo...')
    return True


if __name__ == '__main__':
    game = Game()
    game.play()