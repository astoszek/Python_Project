import random

number = random.randint(1, 10)
msg = "Zgadnij jaka liczbe mam na myśli od 1 do 10: "
guess = int(input(msg))

if guess == number:
    print("Gratulacje")
