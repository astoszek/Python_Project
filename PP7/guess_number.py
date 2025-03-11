# import random
#
# number = random.randint(1, 3)
# guess = int(input("Zgadnij jaka liczbe mam na myśli (1 ,2 3):"))
#
# if guess == number:
#     print("Brawo. Taką liczbe miałem na myśli")
# else:
#     print("Niestety myślałem o liczbię " + str(number) + ".")

import random
number = random.randint (1, 3)

guess = int(input("Guess a number:  1, 2,3"))

if guess == number:
    print("brawo")
else:
    print("jestes chujem")