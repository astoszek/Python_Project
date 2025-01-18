def remove_dupliactes(my_list_1):
    return list(set(my_list_1))

my_list_1 = ["Ala", "Zosia", "Zosia", "Mirek"]
my_list_2 = remove_dupliactes(my_list_1)
print(my_list_2)