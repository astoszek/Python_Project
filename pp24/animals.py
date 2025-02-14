class Animal:
    def introuduce(self):
        print(f"Jestem typem {self.type} mam na imię {self.name}, jest nas {self.counter}.")


class Dog(Animal):
    type = "pies"
    counter = 0

    def __init__(self, name):
        self.name = name
        Dog.counter += 1


class Cat(Animal):
    type = "kot"
    counter = 0

    def __init__(self, name):
        self.name = name
        Cat.counter += 1


animals = [
    Dog("Pluto"),
    Cat("Filemon"),
    Dog("Azor"),
    Dog("Loki"),
    Cat("Sylwester")
]

for animal in animals:
    animal.introuduce()