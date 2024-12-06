# # for i in range (1, 100):
# #     if i % 3 == 0:
# #         print("Liczby podzielne przez 3 to:" ,str(i))
# rozmiar = int(input("Podak rozmiar macierzy: "))
# znak = input("Podaj znak:" )
#
#
# for i in range (rozmiar):
#     for j in range (rozmiar):
#         print(znak, end="")
#     print()

s = 0
for i in range(64):
    s += 2 ** i

print("Suma wszystkich zairen na szachownicy to: "+ str(s))

#założenia: waga 1 ziarna to 0,4mg -> 0,0004g

# 1kg = 1000g
# 1t = 1000kg


tons = int(s * 0.0004 / 1000 / 1000)

print("W tonach to: ", tons)