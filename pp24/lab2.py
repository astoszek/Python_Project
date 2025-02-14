# Dokonaj modyfikacji programu ze zwierzętami (animals.py):
# • dodaj 2 kolejne dowolne zwierzęta,
# • dodaj metody symulujące wydawanie dźwięków przez zwierzęta np. wyświetlając napis "miau",
# • dodaj właściwość pozwalającą zliczać wszystkie zwierzęta,
# • uwzględnij sumę wszystkich zwierząt oraz wydawane przez zwierzę dźwięki w metodzie introduce().

class Animal:
    all_counter = 0

    def __init__(self):
        Animal.all_counter += 1

    def introuduce(self):
        print(f"Jestem typem {self.type} mam na imię {self.name}, jest nas {self.counter}, a wszystkich zwierząt {self.all_counter}, {self.make_sound()}.")


class Dog(Animal):
    type = "pies"
    counter = 0

    def __init__(self, name):
        super().__init__()
        self.name = name
        Dog.counter += 1

    def make_sound(self):
        return "hau hau"


class Cat(Animal):
    type = "kot"
    counter = 0

    def __init__(self, name):
        super().__init__()
        self.name = name
        Cat.counter += 1

    def make_sound(self):
        return "miau"


class Pig(Animal):
    type = "świnka"
    counter = 0

    def __init__(self, name):
        super().__init__()
        self.name = name
        Pig.counter += 1

    def make_sound(self):
        return "chrum chrum"


class Horse(Animal):
    type = "koń"
    counter = 0

    def __init__(self, name):
        super().__init__()
        self.name = name
        Horse.counter += 1

    def make_sound(self):
        return "ihaaa"


animals = [
    Dog("Pluto"),
    Cat("Filemon"),
    Dog("Azor"),
    Dog("Loki"),
    Cat("Sylwester"),
    Pig("Piggy"),
    Horse("Karino"),
]

for animal in animals:
    animal.introuduce()
