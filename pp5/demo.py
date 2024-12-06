# Definicja funkcji do obliczenia czasu pobierania
def czas_pobierania(rozmiar_pliku_MB, czas_pobierania_s, rozmiar_danych_TB):
    # Oblicz prędkość pobierania w MB/s
    predkosc_MB_s = rozmiar_pliku_MB / czas_pobierania_s

    # Przekształć rozmiar danych z TB na MB (1 TB = 1 000 000 MB)
    rozmiar_danych_MB = rozmiar_danych_TB * 1000000

    # Oblicz czas pobierania w sekundach
    czas_pobierania_s = rozmiar_danych_MB / predkosc_MB_s

    # Przekształć czas w godziny
    czas_pobierania_godziny = czas_pobierania_s / 3600

    # Zaokrąglij do pełnych godzin
    return round(czas_pobierania_godziny)


# Zdefiniowane wartości
rozmiar_pliku_MB = 194  # Rozmiar pliku w MB
czas_pobierania_s = 5  # Czas pobierania pliku w sekundach
rozmiar_danych_TB = 13  # Rozmiar danych w TB

# Obliczenie wymaganych godzin
godziny = czas_pobierania(rozmiar_pliku_MB, czas_pobierania_s, rozmiar_danych_TB)

# Wyświetlenie wyniku
print(f"Czas pobierania danych o rozmiarze {rozmiar_danych_TB} TB wyniesie około {godziny} godzin.")
