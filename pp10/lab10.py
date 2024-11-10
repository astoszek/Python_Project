# 1. Napisz skrypt, pobierający od użytkownika zbiór imion, w tym celu:
#• skrypt powinien zapytać użytkownika o liczbę elementów zbioru,
#• pobrać kolejne elementy i zapisać je do listy,
#• wyświetlić w podsumowaniu jakie imiona pobrał od użytkownika.

liczba_imion = int(input("Podaj liczbę imion: "))
lista_imion = []

for i in range(liczba_imion):
    imie = input("Podaj imię: ")
    lista_imion.append(imie)


print("Pobrano następujące imiona: ", lista_imion)


print("")

liczba_imion = int(input("Podaj liczbę imion: "))
lista_imion = []
for i in range(liczba_imion):
    lista_imion.append(input("Podaj " + str(i +1) + " imię:"))

print("OD użytkownika pobrano następująćy zbiór imion: ", lista_imion)