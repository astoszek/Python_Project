# ciąg Fibonacciego

# 1 1 2 3 5 8 13 21 ...

def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    return fib(n - 1) + fib(n - 2)

for n in range(1, 50):

    print(n, "->", fib(n))
