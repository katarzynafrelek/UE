# Zadanie 1

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        if self.marks > 50:
            return True
        else:
            return False


student1 = Student("Kasia", 85)
student2 = Student("Mateusz", 50)

print(student1.is_passed())
print(student2.is_passed())


# Zadanie 2


class Library:
    def __init__(self, city, street, zip_code, open_hours: str, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f'Biblioteka zlokalizowana jest w miescie {self.city} przy ulicy {self.street}. '\
               f'Jest otwarta w godzinach {self.open_hours}. '\
               f'Telefon kontaktowy: {self.phone}.'


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f'Pracownik {self.first_name} {self.last_name}, urodzony dnia {self.birth_date}. '\
               f'Zatrudniony dnia {self.hire_date}. '\
               f'Adres zamieszkania: ulica {self.street}, {self.city}, {self.zip_code}. '\
               f'Numer telefonu: {self.phone}'


class Student:
    def __init__(self, first_name, last_name, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f'Student {self.first_name} {self.last_name}, urodzony dnia {self.birth_date}. '\
               f'Adres zamieszkania: ulica {self.street}, {self.city}, {self.zip_code}. '\
               f'Numer telefonu: {self.phone}'


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


class Order:
    def __init__(self, employee: Employee, student: Student, books: Book, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return f'Zamowienie studenta {self.student.__str__()} z dnia {self.order_date}: {self.books.__str__()} ' \
               f'Przygotowane przez pracownika: {self.employee.__str__()}.'


library1 = Library("Katowice", "Brynowska", "40-666", "8-16", "700-800-900")
library2 = Library("Warszawa", "Warszawska", "00-666", "7-17", "100-200-300")
#
book1 = Book(library1, "2010", "Stephen", "King", "1738")
book2 = Book(library1, "2018", "Stephen", "King", "312")
book3 = Book(library1, "2021", "Stephen", "King", "1738")
book4 = Book(library2, "2001", "Joanne ", "Rowling", "455")
book5 = Book(library2, "2012", "John", "Tolkien", "1320")
#
employee1 = Employee("Marek", "Kowalski", "20.05.2020", "19.08.1999", "Sosnowiec", "Damrota", "39-250", "555-122-456")
employee2 = Employee("Jan", "Nowak", "01.09.2018", "19.08.1995", "Bedzin", "Pilsudskiego", "42-750", "777-555-444")
employee3 = Employee("Anna", "Czarna", "01.12.2019", "11.02.2001", "Katowice", "Rolna", "40-600", "599-333-888")
#
student1 = Student("Elzbieta", "Szczyrk", "03.09.2004", "Bielsko-Biala", "Fabryczna", "25-600", "111-222-333")
student2 = Student("Kamila", "Szczyrk", "03.09.2004", "Bielsko-Biala", "Fabryczna", "25-600", "111-222-444")
student3 = Student("Mikolaj", "Szczyrk", "03.09.2004", "Bielsko-Biala", "Fabryczna", "25-600", "111-222-555")
#
order1 = Order(employee1, student2, book4, "10.11.2021")
order2 = Order(employee3, student3, book1, "20.11.2021")

print(order1)
print(order2)
