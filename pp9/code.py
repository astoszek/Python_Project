# rozszyfruj wiadomość  Xq|`gf(bm{|(nibfq)
# szyfr: dla każdego znaku zmieniono 4 bit na przeciwny
# bity liczymy od najmniej znaczącego


print(ord("c"), chr(99))

print("{:08b}".format(ord("c")))
# 01100011 -> chcemy zmienić 4 bit (od prawej) na przeciwny
# 00001000 -> maska pozwalana nam wyizolować dany bit
# 01101011 -> używamy XORa (aletrnatywa rozłączna), do zmiany bitu

print("{:08b}".format(1 << 3))
print("{:08b}".format(ord("c") ^ (1 << 3)))
str ="Xq|`gf(bm{|(nibfq)"
for c in str:
    n = ord(c) ^ (1 << 3)
    print(chr(n), end="")