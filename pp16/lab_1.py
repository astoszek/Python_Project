import platform
import math
from random import sample


def draw_numbers():
    numbers = [i for i in range(1, 11)]
    unique_numbers = sample(numbers, 3)
    return unique_numbers


def machine():
    return (platform.machine())


def sinus():
    print(math.sin(90))


if __name__ == '__main__':
    print(draw_numbers())
    print(machine())
    print(sinus())