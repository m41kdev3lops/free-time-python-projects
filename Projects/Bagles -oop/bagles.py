import random


class Bagles:

    def __init__(self, diff):
        if diff == 'r' or int(diff) > 9:
            diff = random.randint(1, 9)
        self.diff = int(diff)


    @property
    def newGame(self):
        secret_number = self.getRandomNumber
        return secret_number


    @property
    def getRandomNumber(self):
        ALL_NUMBERS = list(range(10))
        random.shuffle(ALL_NUMBERS)
        SECRET_NUMBER = ALL_NUMBERS[:self.diff]
        return SECRET_NUMBER


    def validateInput(self, value):
        try:
            value = str(value)
            if len(value) != int(self.diff):
                return False
            else:
                int(value)
                return True
        except:
            return False