# Program symulujacy rzuty dwiema kostkami do gry
# Rzucamy dwiema kostkami do momentu aż nie wyrzucimy dubletu

import random


class Dice:
    def __init__(self):
        self.Value = None

    def throw(self):
        self.Value = random.randint(1, 6)

    def __str__(self):
        return f"[{self.Value}]"  # np [3]


class DicePair(Dice):

    def __init__(self):
        self.pair = [Dice(), Dice()]

    def throw(self):
        self.pair[0].throw()
        self.pair[1].throw()

    def __str__(self):
        return str(self.pair[0]) + str(self.pair[1])

    def is_double(self):
        return self.pair[0].Value == self.pair[1].Value


dices = DicePair()
counter = 1
while True:
    dices.throw()
    print(counter, dices)
    if dices.is_double():
        break
    counter += 1
