# Dokonaj odpowiednich zmian w programie do rzucania kośćmi do gry (dices.py), aby
# zabezpieczyć zmienne instancji przed przypadkowym nadpisaniem (enkapsulacja).


import random


class Dice:
    def __init__(self):
        self.__Value = None

    def get_Value(self):
        return self.__Value

    def throw(self):
        self.__Value = random.randint(1, 6)

    def __str__(self):
        return f"[{self.__Value}]"  # np [3]


class DicePair(Dice):

    def __init__(self):
        self.__pair = [Dice(), Dice()]



    def throw(self):
        self.__pair[0].throw()
        self.__pair[1].throw()

    def __str__(self):
        return str(self.__pair[0]) + str(self.__pair[1])

    def is_double(self):
        return self.__pair[0].get_Value() == self.__pair[1].get_Value()


dices = DicePair()
counter = 1
while True:
    dices.throw()
    print(counter, dices)
    if dices.is_double():
        break
    counter += 1
