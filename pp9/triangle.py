#Pobieramy od użytkownika długośći 3 odcinków
#Sprawdź czy można z nich zbudować trójkąt
#Sprawdź jaki to bedzie trójkąt ze względu na boki (różnoboczny, równoboczny, równoramienny)
#Sprawdź jaki to będzie trójkąt ze względu na kąty (prostokątny, ostrokątny, rozwarty)

print("Podaj długośći 3 odcinków (liczby całkowite)")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if a + b > c and a + c > b and b + c > a:
    print ("Z tych odcinków można zbuodować trójkąt", end="")
    if a == b  and a == c and b == c:
        print(" równoboczny ", end="")
    elif a == b or  a == c or b == c:
        print(" równoramienny ", end="")
    else:
        print(" różnoramienny ", end="")
    if a ** 2 + b ** 2 == c ** 2 or b ** 2 + c ** 2 == a ** 2 or c ** 2 + a ** 2 == b ** 2:
        print("Powstanie trojkat prostokątny")
    elif a ** 2 + b ** 2 < c ** 2 or b ** 2 + c ** 2 < a ** 2 or c ** 2 + a ** 2 < b ** 2:
        print("Powstanie trojkat rozwartokątny")
    else:
        print("powstanie trojkat ostrokątny")
else:
    print("Z tych odcinkow nie mozna zbudowac trojkata")