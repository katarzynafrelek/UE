class Property:
    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address


class House(Property):
    def __init__(self, area, rooms: int, price, address, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f'Budynek zlokalizowany pod adresem: {self.address} w dzielnicy {self.area} ' \
               f'na dzialce o powierzchni  {self.plot} m2. ' \
               f'Liczba pokoi: {self.rooms}. ' \
               f'Proponowana cena: {self.price} zl.'


class Flat(House):
    def __init__(self, area, rooms: int, price, address, plot: int, floor):
        super().__init__(area, rooms, price, address, plot)
        self.floor = floor

    def __str__(self):
        return f'Mieszkanie zlokalizowane pod adresem: {self.address} w dzielnicy {self.area} ' \
               f'na dzialce o powierzchni  {self.plot} m2. ' \
               f'Liczba pokoi: {self.rooms}. ' \
               f'Pietro: {self.floor}. '\
               f'Proponowana cena: {self.price} zl. '


house1 = House("Kostuchna", 3, "350 tys.", "Sezamkowa 20,40-999 Katowice", 200)
flat1 = Flat("Kostuchna", 3, "350 tys.", "Sezamkowa 20,40-999 Katowice", 200, 2)

print(house1)
print(flat1)
