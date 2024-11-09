number = 1

if number > 0:
    print("Liczba jest większa od 0")
elif number < 0:
    print("Liczba mniejsza od 0")
else:
    print("Liczba równa 0")


number = int(input("Podaj liczbę całkowitą: "))
if number  ** (0.5) % 1 == 0:
    print("Pierwiastek kwadratowy z liczby", number, "jest liczbą całkowitą.")
else:
    print("Pierwiastek kwadratowy z liczby", number, "nie jest liczbą całkowitą.")

number = int(input("Podaj liczbę całkowitą: "))
if number ** (0.5) % 1 == 0:
    str1 = "Tak"
    str2 = ""
else:
    str1 = "Nie"
    str2 = "Nie"

print(str1 + "Pierwiastek kwadratowy z libczy  ")