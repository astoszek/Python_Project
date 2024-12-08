# # # # numbers = (1, 2, 3)
# # # #
# # # # print(numbers)
# # #
# # # numbers = tuple(x for x in range(10) if x % 2 ==0)
# # #
# # # print(numbers)
# #
# # letters = tuple("Ala ma kota.")
# # print(letters)
#
# phones ={"Tomek": 555678987, "Ada": 123123123, "Karol":456789456}
# print(phones)

animals_dict = {
    "kot": "cat",
    "pies": "dog",
    "chomik": "hamster"
}

animals_dict["świnka"] = "pig"
print(animals_dict)
animals_dict.popitem()
print(animals_dict)

# print(animals_dict["kot"])
# print(animals_dict.get("kot"))


words = ["kot", "lew", "chomik"]

# for word in words:
#     if word in animals_dict.keys():
#         print(word, "->", animals_dict[word])
#     else:
#         print("Nie znalezniono słowa {} w słowniku".format(word))

for key in animals_dict.keys():
    print(key, "->", animals_dict[key])

print()

for value in animals_dict.values():
    print(value)

for pl, en in animals_dict.items():
    print(pl, "->", en)