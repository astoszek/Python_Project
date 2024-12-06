# Liczby całkowite


print(1_000_000)
print(-2)
print(type(2.45))

# systemy liczbowe
# dziesiętnie: 123 = 1 * 10 ** 2 + 2 * 10 ** 1 + 3 * 10 ** 0

print(0b101) #literał w systemie dwójkowym
print(0o14) #literał w systemie ósemkowym
print(0xFF) #szesnastkowy

print(0o12 + 0xA)

print(type(0o127))


# liczby zmienno przecinkowe

print(2.0)
print(2, 0)
print(.123)

print(5e3)  # 5 *10 ** 3 + 5 *1000 = 5000
print(1e17)
print(2.45e-4)

print(123_000_000)
print("{:.2e}".format(123_000_000))

print(2.3e-5)
print("{:.6f}".format(2.3e-5))


# ciągi znaków

print("Ala ma kota, a kot ma Alę.")
print('Ala ma kota, a kot ma Alę.')
print("tekst ze \nznakiem nowej linii")

print("I'm Monty Python.")

print("><", ">\t<", ">\t\t\t<", sep="\n")

print(type(" "))


# wartośći logiczne (boolowskie)

print(False)
print(2 >3)
print(type(2 >3))
print(type(3>2))
print(2 < 3)

print(bool(1))
print(bool(13))
print(bool(0))