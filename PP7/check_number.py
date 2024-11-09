# Skyrpt pobiera liczbe od użytkownika
# wyświetla informacja czy dana liczba jest parzysta, podzielna przez 5 i 7

number =  int(input("Podaj liczbe:  "))
print("Liczba jest: ")

if number % 2 == 0:
    print(" - parzysta")
else:
    print(" - nieparzysta")

if number % 5== 0:
    print(" - jest podzielna przez 5")
else:
    print(" - nie jest podzielna przez 6")

if number % 7 == 0:
    print(" - jest podzielna przez 7")
else:
    print(" - nie jest podzielna przez 7    ")