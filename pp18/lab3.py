# Rozszyfruj poniższą wiadomość wiedząc, że została ona zaszyfrowana szyfrem cezara z parametrem przesunięcia równym 3.
# VWXGLD SRGBSORPRZH - SURJUDPLVWD SBWKRQ
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
#

delta = 3
code = "VWXGLD SRGBSORPRZH - SURJUDPLVWD SBWKRQ"

def decode_letter(letter, delta):
    if letter < "A" or letter > "Z":
        return letter
    n = ord(letter) - delta
    if n < ord('A'):
        n += ord('Z') - ord('A') + 1
    return chr(n)


def decode(string, delta):
    decoded = ""
    for letter in string:
        decoded += decode_letter(letter, delta)
    return decoded


print(decode(code, delta))
