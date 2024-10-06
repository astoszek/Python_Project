# 1. Napisz skrypt wyświetlający na ekranie informacje o użytkowniku takie
#jak: imię, wiek oraz miasto. Dane przechowuj w odpowiednio nazwanych
# zmiennych.


imie  = "Arek"
wiek = 30
miasto = "Katowice"

print(imie, wiek, miasto)

print("Mam na imę " + imie +".")
print("Mam", wiek, "lata.")
print("MOje miasto to", miasto + ".")
print(" ")
# 2

#Napisz skrypt obliczający pole powierzchni, obwód oraz długość
#przekątnej dla kwadratów o następujących długościach boku: 2, 7, 11 oraz 19.

a = 2
pole = a ** 2
obwod = a * 4
przekatna_kwadratu = a * 2 ** 0.5

print(" ")
print("Pole kwadratu o dlugosci boku " + str(a) + " to " + str(pole))
print("Obwod kwadratu o dlugosci boku " + str(a) + " to " + str(obwod))
print("Przekatna kwadratu o dlugosci boku " +str(a) + " to " + str(przekatna_kwadratu))


a = 7
pole = a ** 2
obwod = a * 4
przekatna_kwadratu = a * 2 ** 0.5

print(" ")
print("Pole kwadratu o dlugosci boku " + str(a) + " to " + str(pole))
print("Obwod kwadratu o dlugosci boku " + str(a) + " to " + str(obwod))
print("Przekatna kwadratu o dlugosci boku " +str(a) + " to " + str(przekatna_kwadratu))


a = 11
pole = a ** 2
obwod = a * 4
przekatna_kwadratu = a * 2 ** 0.5
print(" ")
print("Pole kwadratu o dlugosci boku " + str(a) + " to " + str(pole))
print("Obwod kwadratu o dlugosci boku " + str(a) + " to " + str(obwod))
print("Przekatna kwadratu o dlugosci boku " +str(a) + " to " + str(przekatna_kwadratu))

a = 19
pole = a ** 2
obwod = a * 4
przekatna_kwadratu = a * 2 ** 0.5
print(" ")
print("Pole kwadratu o dlugosci boku " + str(a) + " to " + str(pole))
print("Obwod kwadratu o dlugosci boku " + str(a) + " to " + str(obwod))
print("Przekatna kwadratu o dlugosci boku " +str(a) + " to " + str(przekatna_kwadratu))


# 3

#Wyznacz zysk z 3 letniej lokaty bankowej wg założeń:
#• inwestowane środki 46 567,00 zł
#• stałe oprocentowanie roczne 7.5%
#• coroczna kapitalizacja odsetek
#• w obliczeniach zastosuj złożony operator przypisania
print(" ")
print(" ")
own_funds = 46_567. #inwestowane środki
deposit = own_funds
factor = 1.075

deposit *= factor
deposit *= factor
deposit *= factor


print("Zysk z inwestycji wynosi", round(deposit - own_funds, 2), "zł.")
