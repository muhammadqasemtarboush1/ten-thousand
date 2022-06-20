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
        self.invalid_answer = False

    def zilch(self, new_roller):
        zilch_check_score = GameLogic.calculate_score(new_roller)
        if zilch_check_score == 0:
            print("****************************************" + '\n' + "**        Zilch!!! Round over         **"
                  + "\n" + "****************************************")
            self.banker.clear_shelf()
            return True
        return False

    def validate_shelfing(self, user_answer):
        if not self.invalid_answer:
            dices = [x for x in user_answer if x.strip() != ""]
            num_of_dice_shelving = len(dices)
            dice_kept = map(int, dices)
            roll_tuple = tuple(dice_kept)
            score = GameLogic.calculate_score(roll_tuple)
            self.banker.shelf(score)
            self.dice -= num_of_dice_shelving
            print(f'You have {self.banker.shelved} unbanked points and {self.dice} dice remaining')
            print('(r)oll again, (b)ank your points or (q)uit:')
        elif self.invalid_answer:
            print('Cheater!!! Or possibly made a typo...')
            dices = [x for x in user_answer if x.strip() != ""]
            num_of_dice_shelving = len(dices)
            dice_kept = map(int, dices)
            roll_tuple = tuple(dice_kept)
            score = GameLogic.calculate_score(roll_tuple)
            self.banker.shelf(score)
            print(f'You have {self.banker.shelved} unbanked points and {self.dice} dice remaining')
            print('(r)oll again, (b)ank your points or (q)uit:')

    def play(self, roller=GameLogic.roll_dice):
        cheating_status = False
        print('Welcome to Ten Thousand')
        print('(y)es to play or (n)o to decline')
        user_answer = input('> ')
        if user_answer == 'n':
            print('OK. Maybe another time')
            return
        if user_answer == 'y':
            print(f'Starting round {self.round}')
        while True:
            if not cheating_status:
                print(f'Rolling {self.dice} dice...')
            new_roller = roller(self.dice)
            formatted_line = "*** " + ' '.join([str(i) for i in new_roller]) + " ***"
            print(formatted_line)
            if self.zilch(new_roller) != True:
                print('Enter dice to keep, or (q)uit:')
                user_answer = input('> ')
                if user_answer == 'q':
                    print(f'Thanks for playing. You earned {self.banker.balance} points')
                    return
                cheating_status = check_cheater(user_answer, new_roller)
                if user_answer != 'q':
                    if not cheating_status:
                        raw_answers = user_answer.strip('1').strip('5').strip()
                        if len(raw_answers) <= 2 and len(
                                raw_answers) != 0 and '5' not in user_answer and '1' not in user_answer:
                            self.invalid_answer = True
                        self.validate_shelfing(user_answer)
                        user_choice = input('> ')
                        if self.dice == 0 and user_choice == "r":
                            self.dice = 6
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
            else:
                print(f'You banked {self.banker.shelved} points in round {self.round}')
                print(f'Total score is {self.banker.balance} points')
                self.round += 1
                print(f'Starting round {self.round}')
                self.dice = 6


def check_cheater(user_answer, roller):
    dice_values = Counter(roller).most_common()
    user_input = Counter(user_answer).most_common()
    # cheating_status = True
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
