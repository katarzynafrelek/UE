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


library1 = Library("Katowice", "Brynowska", "40-666", "8-16", "700-800-900")
library2 = Library("Warszawa", "Warszawska", "00-666", "7-17", "100-200-300")
