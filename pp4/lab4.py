# 1. Ustal, czy liczby 14196 i 14199, są podzielna przez: 3, 4, 7 oraz 13

print(14196 %3 == 0) #jest
print(14196 %4 == 0) #jest
print(14196 %7 == 0) #jest
print(14196 %13 == 0) #jest
print("")
print(14199 %3 == 0) #jest
print(14199 %4 == 0) #nie jest
print(14199 %7 == 0) #nie jest
print(14199 %13 == 0) #nie jest
print("")
print("")
# 2.#Napisz skrypt, który oblicza ile warta byłaby inwestycja na kwotę 14 000 zł, gdyby jej wartość zwiększyła się w pierwszym roku o 40%, w
# drugim roku zanotowała stratę w wysokości 1500 zł, a w trzecim roku  zwiększyła się o 12%.


print(((14000 * 1.4) -1500) * 1.12)
print("")

print("Początkowa wartośc inwestycji", 14_000., "zł")
print("Wartość inwestycji po pierwszym roku", 14_000. * 1.4, "zł")
print("Wartość inwestycji po drugim roku", (14_000. * 1.4) - 1500, "zł")
print("Wartość inwestycji po trzecim roku", ((14_000. * 1.4) - 1500) * 1.12, "zł")

print("")
print("")
# 3.Wylicz wartości dziesiętne następujących liczb zapisanych w różnych  systemach liczbowych

print(0o777)
print(7 *8 ** 2 + 7 * 8 ** 1 + 7 * 8 ** 0)
print("")
print(0b1011)
print(1 * 2 **3 + 0 * 2 ** 2 + 1 * 2 ** 1 + 1 * 2 ** 0)
print("")
print(0xFFF)
print(15 * 16 ** 2 + 15 * 16 ** 1 + 15 * 16 ** 0)
print("")

print(1 * 5 **2 + 2 * 5 ** 1 + 3 *5 ** 0)
print("")

