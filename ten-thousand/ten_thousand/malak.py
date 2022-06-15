def play(self):
    print('Welcome to Ten Thousand')
    print('(y)es to play or (n)o to decline')

    response = input('> ')

    if response == 'n':
        print('OK. Maybe another time')
        return
    else:
        print(f'Starting round {self.round}')
        while True:

            print(f'Rolling {self.dice} dice...')
            roll = self.roller(self.dice)
            print(f'*** {roll}***')
            print('Enter dice to keep, or (q)uit:')
            dice_to_keep = input('> ')
            dices = [x for x in dice_to_keep]

            if dice_to_keep == 'q':
                print(f'Thanks for playing. You earned {self.banker.balance} points')
                running = False
                return

            if dice_to_keep != 'q':
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