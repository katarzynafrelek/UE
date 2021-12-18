from Lab_4_v2.Book import Book, book1, book4
from Lab_4_v2.Employee import Employee, employee1, employee3
from Lab_4_v2.Student import Student, student2, student3


class Order:
    def __init__(self, employee: Employee, student: Student, books: Book, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return f'Zamowienie studenta: {self.student.__str__()} ' \
               f'Zamowienie złozone dnia {self.order_date}: {self.books.__str__()} ' \
               f'Zamowienie przygotowane przez pracownika: {self.employee.__str__()}.'


order1 = Order(employee1, student2, book4, "10.11.2021")
order2 = Order(employee3, student3, book1, "20.11.2021")
