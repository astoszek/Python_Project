while True:
    try:
        number = int(input("Podaj liczbę całkowitą: "))
        print("Odwrotna liczba to", 1 /number )
    except ValueError:
        print("To nie jest liczba całkowita.")
    except ZeroDivisionError:
        print("Błąd dzielenie przez 0.")
    except:
        print("Coś poszło nie tak...")