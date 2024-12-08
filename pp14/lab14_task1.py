catalog = {
    "Anna": 123456789,
    "Jan": 987654321,
    "Arek": 555666777,
    "Michał": 444555666
}

name = input("Podaj imię: ")

if name in catalog.keys():
    print("Numer telefonu osoby", name, "->", catalog[name])
else:
    print("Nie znaleziono numeru telefonu dla osoby o imieniu", name)
