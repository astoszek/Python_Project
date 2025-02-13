# # liczba_imion = int(input("Podaj liczbe imion: "))
# # imiona = []
# #
# # for i in range(liczba_imion):
# #     imiona.append(input("Podaj " + str(i + 1) + " imię:"))
# #
# # print("Użytkownik podał następujące imiona", imiona)
#
#
# import random
#
# DICE_ROLLS_TOTAL = 16
# rolls = []
#
# for i in range(DICE_ROLLS_TOTAL):
#     rolls.append(random.randint(1, 6))
#
# print("Zbiór wyników po", DICE_ROLLS_TOTAL, "rzutach kostka to ", rolls)
#
# print()
#
# print("Za ósmym razem wyrzucono ", str(rolls[8 - 1]))
#
# sixes_total = 0
#
# for roll in rolls:
#     if roll == 6:
#         sixes_total += 1
# print()
# print("Szóstka pojawia się", int(sixes_total) , "razy")
#
# in_row_value_tmp = rolls[0]
# in_row_total_tmp = 0
# in_row_value = 0
# in_row_total = 0
#
#
# for roll in rolls:
#     if roll == in_row_value_tmp:
#         in_row_total_tmp += 1
#     else:
#         in_row_value_tmp = roll
#         in_row_total_tmp = 1
#     if in_row_total_tmp > in_row_total:
#         in_row_value = in_row_value_tmp
#         in_row_total = in_row_total_tmp
#
#
# print("Pod rząd wyrzucono", in_row_total, "razy wartość", str(in_row_value) + ".")


