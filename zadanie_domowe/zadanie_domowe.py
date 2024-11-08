#1. Wyświetl na ekranie następujący wzór:

print("*        *")
print("**      **")
print("***    ***")
print("****  ****")
print("**********")
print("****  ****")
print("***    ***")
print("**      **")
print("*        *")

print("")
print("")
print("")

#2. Napisz skrypt pomagający oszacować ile godzin potrzeba na pobranie
#danych z sieci o rozmiarze 13 TB, jeżeli wiesz, że plik o rozmiarze 194 MB
#udało się pobrać w 5 sekund. Wynik zaokrąglij do pełnych godzin.

print("Prędkość pobierania:" , 194 / 5)
print("Czas pobierania w sekundach:" , 13000000 / 38.8)
print("Czas pobierania w godzinach:" , 335051.5463917526 // 3600)
print("")
print("")
print("")
"""
3. Napisz skrypt pozwalający zasymulować zyski z lokat bankowych przy
następujących założeniach:
• własne środki 30 tys. zł,
• roczna lokata kapitału,
• kwartalna kapitalizacja odsetek (saldo będzie aktualizowane co 3 miesiące),
• oprocentowanie roczne dla 3 wariantów: 7,5%, 8% oraz 8,25%,
• pokazać salda po każdym kwartale,
• wyliczyć roczny zysk.
"""


own_funds = 30_000 #inwestowane środki
deposit = own_funds
roczne = 1.075

deposit *= roczne
zysk_kwart = (deposit - own_funds) / 4
zysk_roczny = zysk_kwart * 4

print("Zysk kwartalny", zysk_kwart ,"zł")
print("Saldo po pierwszym kwartale przy 7,5% oprocentowaniu to", ((deposit - own_funds) / 4 +30_000 ),"zł.")
print("Saldo po drugim kwartale przy 7,5% oprocentowaniu to", ((deposit - own_funds) / 4 +30_000 + zysk_kwart),"zł.")
print("Saldo po trzecim kwartale przy 7,5% oprocentowaniu to", ((deposit - own_funds) / 4 +30_000 + (2 * zysk_kwart)),"zł.")
print("Saldo po roku przy 7,5% oprocentowaniu to", ((deposit - own_funds)  + 30_000), "zł.")
print("Zysk roczny-" , zysk_roczny ,"zł")

print("")
print("")
print("")

own_funds = 30_000 #inwestowane środki
deposit = own_funds
roczne = 1.080

deposit *= roczne
zysk_kwart = (deposit - own_funds) / 4
zysk_roczny = zysk_kwart * 4

print("Zysk kwartalny", zysk_kwart ,"zł")
print("Saldo po pierwszym kwartale przy 8% oprocentowaniu to", ((deposit - own_funds) / 4 +30_000 ),"zł.")
print("Saldo po drugim kwartale przy 8% oprocentowaniu to", ((deposit - own_funds) / 4 +30_000 + zysk_kwart),"zł.")
print("Saldo po trzecim kwartale przy 8% oprocentowaniu to", ((deposit - own_funds) / 4 +30_000 + (2 * zysk_kwart)),"zł.")
print("Saldo po roku przy 8% oprocentowaniu to", ((deposit - own_funds)  + 30_000), "zł.")
print("Zysk roczny-" , zysk_roczny ,"zł")
print("")
print("")
print("")

own_funds = 30_000 #inwestowane środki
deposit = own_funds
roczne = 1.085

deposit *= roczne
zysk_kwart = (deposit - own_funds) / 4
zysk_roczny = zysk_kwart * 4

print("Zysk kwartalny", zysk_kwart ,"zł")
print("Saldo po pierwszym kwartale przy 8,5% oprocentowaniu to", ((deposit - own_funds) / 4 +30_000 ),"zł.")
print("Saldo po drugim kwartale przy 8,5% oprocentowaniu to", ((deposit - own_funds) / 4 +30_000 + zysk_kwart),"zł.")
print("Saldo po trzecim kwartale przy 8,5% oprocentowaniu to", ((deposit - own_funds) / 4 +30_000 + (2 * zysk_kwart)), "zł.")
print("Saldo po roku przy 8,5% oprocentowaniu to", ((deposit - own_funds)  + 30_000.), "zł.")
print("Zysk roczny-" , zysk_roczny ,"zł")