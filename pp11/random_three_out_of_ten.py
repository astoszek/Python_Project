# wylosuj 3 liczby ze zbioru 1-10. bez powtózeń posortuj wynik
"""
import random
randonm_numbers = []
counter = 3
while counter:

    number = random.randint(1, 10)
    if number not in randonm_numbers:
        randonm_numbers.append(number)
        counter -= 1
randonm_numbers.sort()
print(randonm_numbers)
"""

import random

numbers = [i for i in range(1, 11)]
random_numbers = random.sample(numbers, k=3) #losowanie liczb ze zbioru bez powtórzeń
random_numbers.sort()
print(random_numbers)