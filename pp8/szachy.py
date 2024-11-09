# 3. Załóżmy, że na pierwsze pole szachownicy kładziemy 1 ziarno zboża, na
# drugie 2 ziarna, na trzecie 4 ziarna i na każde następne pole dwa razy
# więcej ziaren niż na pole poprzednie. Napisz program, który zasymuluje
# taką sytuację i zliczy sumę wszystkich ziaren na szachownicy.

#01 1 2 3 4 5...
#1 2 4 8 16 32 ***

s = 0
for i in range (64):
    s += 2 ** i
    print(s)

print("Suma wszystkich ziaren zboża na szachownicy: " + str(s))


#założenia: waga 1 ziarna to 0,4 mg -> 0,0004g
# 1kg = 1000 g
# 1t = 1000 kg

tons = int(s * 0.004 / 1000 / 1000)

print("To będzie" , tons , "ton.")

# Roczna produkcja pszenicy na świece to 782 mln ton

years = int(tons / 782_000_000)
print("Lata: " ,years)

#Pociąg może przetransportować 2200t

trains = int(tons / 2200)
print("Pociągów: " ,trains)