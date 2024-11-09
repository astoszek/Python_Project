#is_sun_shining = False

#Jeżeli bedzie dodatnia temperatura i bedzie słonecznie to pójdziemy na spacer.
# pójdziem
#if temp > 0 and is_sun_shining:
#    print("Idziemy na spacer")
#else:
 #   print("Zostajemy w domu")

  #  print("-" * 20)

#jeżeli bedzie ujemna temperatura lub bedzie pochmurnie to...
#zostaniemy w domu a jeżeli nie to pójdziemy na spacer


#if not(temp < 0 or not is_sun_shining):
#    print("Idziemy na spacer")
#else:
#    print("Zostajemy w domu")


#operatory logiczne
#and - koniunkca - czytamy jak i
#or - alternatywa - czytamy jak lub
# not - negacja - czytamy jak nie


#iterujemy od 0-9 ( 10 iteracJI0
#wyświetlamy cyfre chyba że,...
#liczba parzysta lub liczba większ od 6 to wyświetl *

#for i in range(10):
#    if i % 2 == 0 or i > 6:
#        print("*")
#    else:
#        print(i)



#a, b, c = 2, 3, 4

#if a < b and b < c:
#    print("!!!")

#a = 5
#b = 3

# koniunkcja bitowa
#print(a, "&", b, "=", a & b)
#print("{:08b}".format(a))
#print("{:08b}".format(b))
#print("{:08b}".format(b))
#print("-" * 8)
#print("{:08b}".format(a & b))

a = 5
b = 3

# alternatywa bitowa
print(a, "|", b, "=", a | b)
print("{:08b}".format(a))
print("{:08b}".format(b))
print("-" * 8)
print("{:08b}".format(a | b))
print("")

# alternatywa rozłączna bitowa
print(a, "^", b, "=", a ^ b)
print("{:08b}".format(a))
print("{:08b}".format(b))
print("-" * 8)
print("{:08b}".format(a ^ b))
print("")
# przesunięcie bitowe w prawo
print(a, ">>", b, "=", a >> b)
print("{:08b}".format(a))
print("-" * 8)
print("{:08b}".format(a >> b))
print("")

# przesunięcie bitowe w lewo
print(a, "<<", b, "=", a << b)
print("{:08b}".format(a))
print("-" * 8)
print("{:08b}".format(a << b))
print("")


# negacja bitowa
print("~" +str(a), "=", ~a)
print("{:08b}".format(a))
print("-" * 8)
print("{:08b}".format(~a))
print("")