# 1.Napisz skrypt sprawdzający czy pierwiastek kwadratowy z liczby całkowitej
# pobranej od użytkownika jest także liczbą całkowitą.

import math

# Pobranie liczby całkowitej od użytkownika
liczba = int(input("Podaj liczbę całkowitą: "))

# Sprawdzenie, czy pierwiastek kwadratowy jest liczbą całkowitą
pierwiastek = math.sqrt(liczba)

if pierwiastek.is_integer():
    print("Pierwiastek kwadratowy z liczby", liczba , "jest liczbą całkowitą.")
else:
    print("Pierwiastek kwadratowy z liczby", liczba , "nie jest liczbą całkowitą.")

# 2. Napisz skrypt wyznaczający ocenę jaką otrzyma student, ze względu na ilość otrzymanych punków z kolokwium:
# • ocena bardzo dobra (5,0), jeżeli student otrzymał 95 lub więcej punktów,
# • jeżeli punktów jest mniej niż 95, ale więcej niż 84 studentowi przysługuje ocena ponad dobra (4,5),
# • ocena dobra (4,0) przyznawana jest dla ilości punktów z przedziału [70, 84],
# • jeżeli student otrzymał więcej niż 60 ale mniej niż 70 to przysługuje mu ocena dość dobra (3,5),
# • ocena dostateczna jest dla studentów z punktowym wynikiem równym przynajmniej 60 ale powyżej 50 punktów,
# • wszystkie wyniki równe 50 i mniej punktów wiążą się z otrzymaniem oceny niedostatecznej (2.0)

number =  int(input("Podaj wynik:  "))
print("Ocena: ")