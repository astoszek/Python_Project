print(~1)
#0000001 (1) => 11111110 (-2)


for i in range(5, -6, -1):
    print("{0:08b} => {1:d}".format(i & 255, i))