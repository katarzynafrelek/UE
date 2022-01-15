class Dom:
    def __init__(self, address: str, rooms: str, surface: float, price: float):
        self._address = address
        self._rooms = rooms
        self._surface = surface
        self._price = price

    def __str__(self):
        return f'Dom mieszczacy sie przy ulicy {self._address} o powierzchni {self._surface} m2. ' \
               f'Liczba pokoi: {self._rooms}. Cena: {self._price} zl.'

    @property
    def get_address(self):
        return self._address

    @property
    def get_rooms(self):
        return self._rooms

    @property
    def get_surface(self):
        return self._surface

    @property
    def get_price(self):
        return self._price
