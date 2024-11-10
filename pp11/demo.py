#a = 1
#b = 4

##a, b = b, a

#print("a =", a, "b =", b)

#numbers = [1, 2, 3]
#numbers[0], numbers[1] = numbers[1], numbers[0]

#print(numbers)


# [4, 5, 2, 1]

# [4, 2, 1, 5]
# [2, 4, 1, 5]
# [1, 2, 4, 5]

#numbers = [4, 5, 2, 1, 3, 123, 9, 40, 39, 38, 100, 0, 0, 0, 111]
#numbers.sort(reverse=True)
#print(numbers)

#numbers = ["C", "A", "B"]
#numbers.sort(reverse=True)
#print(numbers)

#numbers = ["C", "A", "B"]
#numbers.sort(reverse=False)
#print(numbers)

"""
list_1 = [9]
list_2 = list_1 #kopiuje nazwe listy a nie zawartość (2 nazwy ale 1 lista)
list_2[0] = 13
print(list_1)
list_1 = [9]
list_2 = list_1[:] #kopiuje całą liste
list_2[0] = 13
print(list_1)

# wycinki (slicing)
# lista[start:end]
numbers = [10, 8, 6, 4, 2]
new_numbers = numbers[1:4]

print(new_numbers)

# wycinki (slicing)
# lista[start:end]
numbers = [10, 8, 6, 4, 2]
new_numbers = numbers[-4:-1]

print(new_numbers)

# wycinki (slicing)
# lista[start:end]
numbers = [10, 8, 6, 4, 2]
del numbers[-2:]

print(numbers)

# operatory in, not_in
numbers = [1, 2, 3, 4, 5]
print(5 in numbers)
print(6 not in numbers)

#wyrażenia listowe
numbers = []
for i in range(1, 101):
    numbers.append(i)
print(numbers)

numbers = [1 for i in range(1, 101)]
print(numbers)
numbers = [99 for _ in range(1, 101)]
print(numbers)
numbers = [i ** 2 for i in range(1, 101)]
print(numbers)

numbers = [i for i in range(1, 101) if i % 2 == 0]
print(numbers)

# 1-300 ile liczb podzielnych przez 3 i 7
print(len([i for i in range(1, 301) if i % 3 == 0 and i % 7 == 0]))
print(([i for i in range(1, 301) if i % 3 == 0 and i % 7 == 0]))



print([[1, 2], [3, 4]])
row = [1, 2]
matrix = [row, row]
print(matrix)

matrix[0][0] = 99
print(matrix)

print([[1, 2], [3, 4]])
row = [1, 2]
matrix = [row[:], row[:]]
print(matrix)

matrix[0][0] = 99
print(matrix)
"""

