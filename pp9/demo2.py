# for i in range (50):
#     if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
#         print(i)

counter = 0
for i in range (0, 101):
    if i % 2 == 0 and i > 90:
        counter += 1
    elif i % 2 != 0 and i % 9 == 0:
        counter +=1
print("Tych liczb jest :", counter)
print("")
print("")
print("")


counter = 0

for i in range(0, 101):
    if i % 2 == 0 and i > 90:
        print(i)
        counter += 1
    elif i % 2 != 0 and i % 9 == 0:
        print(i)
        counter += 1

print("Tych liczb jest", counter)

print("")
print("")

counter = 0

for i in range(0, 101):
    if (i % 2 == 0 and i > 90) or (i % 2 !=0 and i % 9 ==0):
        counter += 1


print("Takich liczb jest", str(counter))