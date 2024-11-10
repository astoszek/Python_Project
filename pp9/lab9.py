# 1. Wyświetl tylko liczby podzielne przez 3, 5 lub 7, ze zbioru liczb z zakresu określonego przez użytkownika

for i in range(50):
    if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
        print(i)

print("")
print("")

zakres_poczatkowy = int(input("Podaj poczatkowy zakres zbioru: "))  # range_from
zakres_koncowy = int(input("Podaj koncowy zakres zbioru: "))  # range_to

is_first = True

# trzeba zwiekszyc zakres + 1 bo tak dziala petla for.
print("Liczby z zakresu od", zakres_poczatkowy, "do", zakres_koncowy, "podzielne przez 3 lub 5 lub 7 to:", end=" ")
for i in range(zakres_poczatkowy, zakres_koncowy + 1):
    if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
        if not is_first:
            print(", ", end="")
        print(i, end="")
    is_first = False
print(".")

# 2.Udowodnij, że w zbiorze liczb z zakresu 1-100, jest 11 liczb, które są  parzyste i jednocześnie większe od 90, a gdy są nieparzyste, to przynajmniej dzielą się przez 9.
print("")
print("")
print("")
counter = 0

for i in range(0, 101):
    if i % 2 == 0 and i > 90:
        print(i)
        counter += 1
    elif i % 2 != 0 and i % 9 == 0:
        print(i)
        counter += 1

print("Tych liczb jest", counter)

print("")
print("")

counter = 0

for i in range(0, 101):
    if (i % 2 == 0 and i > 90) or (i % 2 !=0 and i % 9 ==0):
        counter += 1


print("Takich liczb jest", str(counter))
#print("Takich liczb jest", counter)

#3 Napisz program wyznaczający wartość n-tego bitu dla dowolnej liczby  całkowitej. Bity liczymy od 0, od najmniej znaczącego bitu.


#print("{:08b}").format (15)