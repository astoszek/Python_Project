# Zaimplementuj funkcję, która przyjmuje jako argument ciąg znaków i zwraca liczbę wystąpień każdego znaku w ciągu.
# Na przykład dla ciągu "abracadabra" funkcja powinna zwrócić słownik { 'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1 }.
txt = """W Pacanowie kozy kują
    więc Koziołek, mądra głowa,
    błąka się po całym świecie,
    aby dojść do Pacanowa.
    Właśnie nową zaczął podróż,
    by ją skończyć w Pacanowie."""
def count_letters(string):
    stats = {}
    for letter in string:
        stats[letter] = stats.get(letter, 0) + 1
    return stats

print(count_letters('abracadabra'))
print(count_letters('Ala ma kota.'))
print(count_letters(txt))

