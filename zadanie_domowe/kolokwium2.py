#Wyświetl tylko liczby podzielne przez 3 ze zbioru liczb z zakresu określonego przez użytkownika.
# Przykładowo dla zakresu od 1 do 10 będą to liczby 3 6 i 9.

liczba = int(input("Podaj liczbe: "))

for i in range(liczba):
    if (i) % 3 == 0:
        print("Te liczby to: ", i)