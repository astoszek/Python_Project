# # # # import math
# # # # import sys
# # # #
# # # # print(math.pi)
# # # # print(math.sin(math.pi / 2))
# # # # print(math.factorial(5))
# # #
# # # # import math as m
# # # # print(m.pi)
# # # #
# # # # from math import pi as PI
# # # # print(PI)
# # #
# # # import random
# # #
# # # print(random.random())
# #
# # from random import random, seed
# #
# # seed(0)
# #
# # for i in range(50):
# #     print(random())
#
# from random import choice, sample
# lst = [i for i in range(1, 11)]
#
# print(choice(lst))#wybiera jedna liczbe ze zbioru
# print(sample(lst, 5))#wybiera  5 liczb ze zbioru bez powtózeń


import platform


print(platform.machine())
print(platform.version())
print(platform.system())
print(platform.python_implementation())
print(platform.python_version_tuple())
