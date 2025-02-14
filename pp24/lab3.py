class Employee:
    def __init__(self, name, position):
        self.__name = name
        self.__position = position

    def introduce(self):
        return f"Jestem {self.__name}, moja pozycja to {self.__position}."

    def get_name(self):
        return self.__name


class Manager(Employee):
    def __init__(self, name, project):
        super().__init__(name, "Manager")
        self.__project = project

    def introduce(self):
        return f"{super().introduce()} Prowadzę projekt: {self.__project}."


class Worker(Employee):
    def __init__(self, name, salary):
        super().__init__(name, "Pracownik")
        self.__salary = salary

    def introduce(self):
        return f"{super().introduce()} Moje wynagrodzenie to {self.__salary} zł."


class Person(Employee):
    def __init__(self, name):
        super().__init__(name, "Osoba")

    def introduce(self):
        return f"{super().introduce()} Nie posiadam wynagrodzenia ani projektu."



people = [
    Manager("Arek Stoszek", "Tajny Projekt x"),
    Worker("Jan Nowak", 4000),
    Person("Janusz Kowalskii"),
    Manager("Ewa Krak", "Tajny Projekt Y"),
    Worker("Jaroslaw Tusk", 3000),
    Person("Mateusz Michalski")
]


for person in people:
    print(person.introduce())