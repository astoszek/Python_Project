# # Napisz skrypt obliczający obwód, pole powierzchni i długość przekątnej dla
# # prostokątów o następujących długościach boków:
# # • 4 i 5,
# # • 2678 i 5678,
# # • 344555 i 788998
#
# def pole(a, b):
#     pole = a * b
#     return pole
#
#
# def obwod(a, b):
#     obwod = (2 * a) + (2 * b)
#     return obwod
#
#
# def przekatna(a, b):
#     przekatna = (a ** 2 + b ** 2) ** 0.5
#     return przekatna
#
#
# print(obwod(4, 5))
#
#

def perimeter(a, b):
    return 2 * a + 2 * b

def surface_area(a, b):
    return a * b

def diagonal_lenght(a, b):
    return (a ** 2 + b ** 2) ** 0.5

def show_result(a, b):
    print("Prostokąt o bokach {} i {}".format(a, b))
    print("Obwód:", perimeter(a,b))
    print("Pole powierzchni: ", surface_area(a,b))
    print("Dlugośc przekątnej: ", diagonal_lenght(a,b))
    print()

show_result(4,5)
show_result(2678,5678)
show_result(344555,788998)