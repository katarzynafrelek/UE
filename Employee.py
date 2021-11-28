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
        return f'{self.first_name} {self.last_name} (ur. dnia {self.birth_date}), '\
               f'zatrudniony dnia {self.hire_date}. '\
               f'Adres zamieszkania: ulica {self.street}, {self.city}, {self.zip_code}. '\
               f'Tel: {self.phone}'


employee1 = Employee("Marek", "Kowalski", "20.05.2020", "19.08.1999", "Sosnowiec", "Damrota", "39-250", "555-122-456")
employee2 = Employee("Jan", "Nowak", "01.09.2018", "19.08.1995", "Bedzin", "Pilsudskiego", "42-750", "777-555-444")
employee3 = Employee("Anna", "Czarna", "01.12.2019", "11.02.2001", "Katowice", "Rolna", "40-600", "599-333-888")
