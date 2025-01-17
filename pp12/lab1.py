def print_char(char="*", repeat=10, vertical=False):
    for i in range(repeat):
        if vertical:
            print(char)
        else:
            print(char + " ", end="")
    print()

print_char()
print_char(char="*", repeat=5, vertical=True)
print_char(char="?", repeat=5, vertical=False)
print_char(char="!", repeat=6, vertical=True)