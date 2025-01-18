"""
Korzystając z odpowiednich modułów napisz skrypt realizujący następujące
zadania:
• wyświetl informacje o procesorze komputera,
• wylosuj 3 niepowtarzalne liczby ze zbioru 1-10,
• wyznacz sinus 90 stopni

"""
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
    print(math.sin(math.radians(90)))


if __name__ == '__main__':
    print(draw_numbers())
    print(machine())
    print(sinus())
