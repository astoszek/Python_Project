# Zaprojektuj klasę reprezentującą osobę (Person) wg założeń:
# • każdy obiekt tej klasy powinien posiadać właściwości: imię oraz wiek,
# • zabezpiecz właściwości obiektu przed przypadkowym nadpisaniem,
# • ustawienie odpowiednich właściwości obiektu powinno następować podczas jego tworzenia,
# • każdy obiekt tej klasy powinien móc wykonać akcję przedstawienia się.


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def introduce(self):
        print("Cześć, jetem", self.__name, "i mam", self.__age, "lat/a.")

persons = []
persons.append(Person("Janek", 23))
persons.append(Person("Agata", 34))
persons.append(Person("Tomek", 55))
persons.append(Person("Monika", 14))

for person in persons:
    person.introduce()