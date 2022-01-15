from Kolokwium2.Klasy_kolokwium.Developer import Developer
from Kolokwium2.Klasy_kolokwium.Dom import Dom
from Kolokwium2.Klasy_kolokwium.Mieszkanie import Mieszkanie


class Zamowienie:
    def __init__(self, order_id: str, developer: Developer, client: str, apartment: Mieszkanie,
                 house: Dom, quantity: int):
        self._order_id = order_id
        self._developer = developer
        self._client = client
        self._apartment = apartment
        self._house = house
        self._quantity = quantity

    def __str__(self):
        return f'Zamowienie numer {self._order_id} pomiedzy deweloperem {self._developer._developer_name}' \
               f' a klientem {self._client}. ' \
               f'Przedmiot zamowienia: {self._apartment.__str__() if self._apartment is not None else ""}' \
               f'{self._house.__str__() if self._house is not None else ""}'

    @property
    def get_order_id(self):
        return self._order_id

    @get_order_id.setter
    def get_order_id(self, setter_input) -> None:
        self._order_id = setter_input

    @property
    def get_client(self):
        return self._client

    @get_client.setter
    def get_client(self, setter_input) -> None:
        self._client = setter_input

    @property
    def get_quantity(self):
        return self._quantity

    @get_quantity.setter
    def get_quantity(self, setter_input) -> None:
        self._quantity = setter_input

    # def order_value_1(self) -> float:
    #     return round((self._apartment.get_price * self._quantity), 2)
    #
    # def order_value_2(self) -> float:
    #     return round((self._house.get_price * self._quantity), 2)

    def order_value_calculation(self):
        if self._apartment is not None and self._house is None:
            tmp_price = self._apartment
        elif self._apartment is None and self._house is not None:
            tmp_price = self._house
        elif self._apartment is not None and self._house is not None:
            return "Zamówienie nie moze posiadac dwoch typow produktu"
        else:
            return "Brak"
        return tmp_price.get_price * self._quantity

    def ordered_surface(self):
        if self._apartment is not None and self._house is None:
            tmp_surface = self._apartment
        elif self._apartment is None and self._house is not None:
            tmp_surface = self._house
        elif self._apartment is not None and self._house is not None:
            return "Zamówienie nie moze posiadac dwoch typow produktu"
        else:
            return "Brak"
        return tmp_surface.get_surface * self._quantity


# Developer1 = Developer("DomBud", "ul. Piekarska 3 Katowice", "123456789", "111122223333")
# Mieszkanie1 = Mieszkanie("ul. Daleka 5 Katowice", "4", 70.5, "3", 899999.00)
# Mieszkanie2 = Mieszkanie("ul. Bliska 5 Chorzow", "3", 35, "8", 490999.99)
# Dom1 = Dom("ul. Wiejska 12 Rybnik", "5", 125.8, 1800999.99)
# Dom2 = Dom("ul. Miejska 9 Bytom", "6", 230, 2350199.59)
# Zamowienie1 = Zamowienie("ZAM1", Developer1, "Jan Kowalski", None, Dom1, 2)

# print(Zamowienie1.__str__())
# print(Zamowienie1.order_value_calculation())
# print(Zamowienie1.ordered_surface())
