# fruits = ["apple", "banana", "cherry"]
# #print(len(fruits) ,fruits)
# #del fruits[0]
# #print(len(fruits) ,fruits)
#
# #print(fruits[2)
#
# # print(len(fruits)) # len() to funkcja
# #
# # fruits.append("plum") # append() to metoda
# #
# # print(fruits)
# #
# # fruits.insert(2, "lemon")
# #
# # print(fruits)
#
#
#
#
#
liczba_imion = int(input("Podaj liczbę imion: "))
lista_imion = []
for i in range(liczba_imion):
    lista_imion.append(input("Podaj " + str(i +1) + " imię:"))

print("OD użytkownika pobrano następująćy zbiór imion: ", lista_imion)