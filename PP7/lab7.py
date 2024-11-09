# 1.Napisz skrypt sprawdzający czy pierwiastek kwadratowy z liczby całkowitej
# pobranej od użytkownika jest także liczbą całkowitą.

number = int(input("Podaj liczbę całkowitą: "))
if number  ** (0.5) % 1 == 0:
    print("Pierwiastek kwadratowy z liczby", number, "jest liczbą całkowitą.")
else:
    print("Pierwiastek kwadratowy z liczby", number, "nie jest liczbą całkowitą.")

# 2. Napisz skrypt wyznaczający ocenę jaką otrzyma student, ze względu na ilość otrzymanych punków z kolokwium:
# • ocena bardzo dobra (5,0), jeżeli student otrzymał 95 lub więcej punktów,
# • jeżeli punktów jest mniej niż 95, ale więcej niż 84 studentowi przysługuje ocena ponad dobra (4,5),
# • ocena dobra (4,0) przyznawana jest dla ilości punktów z przedziału [70, 84],
# • jeżeli student otrzymał więcej niż 60 ale mniej niż 70 to przysługuje mu ocena dość dobra (3,5),
# • ocena dostateczna jest dla studentów z punktowym wynikiem równym przynajmniej 60 ale powyżej 50 punktów,
# • wszystkie wyniki równe 50 i mniej punktów wiążą się z otrzymaniem oceny niedostatecznej (2.0)

number =  int(input("Podaj wynik:  "))
if number >= 95:
    print("Student otrzymał ocene bardzo dobrą")
elif number > 84:
    print("Student otrzymał ocene ponad dobrą")
elif number > 70:
    print("Student otrzymał ocene dobrą")
elif number > 60:
    print("Student otrzymał ocene dość dobrą")
elif number > 50:
    print("Student otrzymał ocene dostateczną")
elif number <= 50:
    print("Student otrzymał ocene niedostateczną")

