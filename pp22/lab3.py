class Book:

    def __init__(self, title, author, publisher, year):
        self.__title = title
        self.__author = author
        self.__publisher = publisher
        self.__year = year

    def show_short_info(self):
        print(f"Tytuł: {self.__title} autor: {self.__author}")

    def show_full_info(self):
        print(f"Tytuł: {self.__title} autor: {self.__author} wydawca {self.__publisher} rok wydania {self.__year}")


books = []
books.append(Book("Dzieci z Bullerbyn", "Astrid Lindgren", "Nasza Księgarnia", 2014))
books.append(Book("Moby Dick", "Herman Marville", "Amercom", 2009))
books.append(Book("Python wprowadzenie", "Mark Lutz", "Helion", 2007))
for book in books:
    book = books()