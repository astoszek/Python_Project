def podnies_do_potegi(lista, potega):
    return [i ** potega for i in lista]

lista = [1, 2, 3, 4]
potega = 3
wynik = podnies_do_potegi(lista, potega)
print(wynik)