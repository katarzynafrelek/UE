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
        return f'{self.first_name} {self.last_name} (ur. {self.birth_date}), '\
               f'adres zamieszkania: ulica {self.street}, {self.city}, {self.zip_code}. '\
               f'Tel: {self.phone}'


student1 = Student("Elzbieta", "Szczyrk", "03.09.2004", "Bielsko-Biala", "Fabryczna", "25-600", "111-222-333")
student2 = Student("Kamila", "Szczyrk", "03.09.2004", "Bielsko-Biala", "Fabryczna", "25-600", "111-222-444")
student3 = Student("Mikolaj", "Szczyrk", "03.09.2004", "Bielsko-Biala", "Fabryczna", "25-600", "111-222-555")
