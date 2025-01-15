# 1. Wyświetl liczby od 1 do 100 z pominięciem liczb podzielnych przez 3

for i in range(1, 101):
    if i % 3 != 0:
        print(i)


# 2.Napisz skrypt wyświetlający na ekranie macierz.
# Rozmiar macierzy oraz znak z jakiej będzie zbudowana powinien określić użytkownik

rozmiar = int(input("Podaj rozmiar: "))
znak = input("Podaj znak: ")

for i in range(rozmiar):
    for j in range(rozmiar):
        print(znak , end="")
    print()

