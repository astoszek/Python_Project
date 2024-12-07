# Popbranie 3 liczb od użytkownika i wyśiwietlnie ich na ekranie

def get_number(number_no):
    print("Proszę Podaj {} liczbę: ".format(number_no))
    return int(input())



print("Pobrano liczby:", get_number(1), get_number(2), get_number(3))

