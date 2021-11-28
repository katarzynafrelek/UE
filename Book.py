from Lab_4_v2.Library import Library, library1, library2


class Book:
    def __init__(self, library: Library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f'Ksiazka autorstwa {self.author_name} {self.author_surname}, ' \
               f'Wydanie z roku {self.publication_date} ' \
               f'(Liczba stron: {self.number_of_pages}). ' \
               f'Dostepna w bibliotece {self.library.__str__()}'


book1 = Book(library1, "2010", "Stephen", "King", "1738")
book2 = Book(library1, "2018", "Stephen", "King", "312")
book3 = Book(library1, "2021", "Stephen", "King", "1738")
book4 = Book(library2, "2001", "Joanne ", "Rowling", "455")
book5 = Book(library2, "2012", "John", "Tolkien", "1320")
