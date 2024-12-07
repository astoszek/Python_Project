# # # # def sum_numbers(numbers):
# # # #     sum = 0
# # # #     for number in numbers:
# # # #         sum += number
# # # #     return sum
# # # #
# # # #
# # # # numbers = [1, 2, 3, 4, 5]
# # # # print(sum_numbers(numbers))
# # #
# # #
# # # def scope_test():
# # #
# # #     x = 123
# # #
# # # scope_test()
# # # print()
# #
# #
# # def scope_test():
# #     x = 999 #zmienna lokalna nadpisała zmienną lokalną
# #     print("w środku funkcji:", x)
# #
# # x = 123
# # scope_test()
# # print("poza funkcjaą", x)
#
#
# def change_value():
#     print("przed zmianą:", n)
#     n += 1
#     print("po zmianie", n)
#
#
# value = 7
# change_value(value)
# print(value)


def change_value(my_list_1):
    my_list_1 = [0, 0]

my_list_2 = [1, 2]
change_value(my_list_2)
print(my_list_2)