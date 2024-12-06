imię = "Arek"
miasto = "Katowice"
wiek = 31

print(imię, miasto, wiek)

print("Mam na imę " ,imię, ".")
print("Mam", wiek, "lata.")
print("MOje miasto to", miasto + ".")
print(" ")


a=2

pole = a **2
obwod = 4 * a
przekatna_kwadratu = a * 2 ** 0.5

print(" ")
print("Pole kwadratu o dlugosci boku " + str(a) + " to " + str(pole))
print("Obwod kwadratu o dlugosci boku " + str(a) + " to " + str(obwod))
print("Przekatna kwadratu o dlugosci boku " +str(a) + " to " + str(przekatna_kwadratu))

print(" ")

own_funds = 46_567. #inwestowane środki
deposit = own_funds
factor = 1.075

deposit *= factor
deposit *= factor
deposit *= factor


print("Zysk z inwestycji wynosi", round(deposit - own_funds, 2), "zł.")