class Banker:
    def __init__(self):
        self.shelved = 0
        self.balance = 0

    ###################
    #  Malak's method
    ###################
    def shelf(self, unbanked):
        self.shelved += unbanked

    ###################
    #  Laila's method
    ###################
    def bank(self):
        # self.balance = 0
        self.balance += self.shelved
        self.shelved = 0
        return self.balance

    ###################
    #  Sondos's method
    ###################
    def clear_shelf(self):
        self.shelved = 0