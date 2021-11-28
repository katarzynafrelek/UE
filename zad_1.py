import street as street


class Produkt:
    def __init__(self, product_name: str, colour: str, producer: str, model: str, product_price: float):
        self.product_name = product_name
        self.colour = colour
        self.producer = producer
        self.model = model
        self.product_price = product_price

    def __str__(self):
        return f'Produkt {self.product_name} model{self.model} marki {self.producer} w cenie {self.product_price}.'


class Magazyn:
    def __init__(self, street: str, city: str, country: str, email: str, phone: str):
        self.street = street
        self.city = city
        self.country = country
        self.email = email
        self.phone = phone

    def __str__(self):
        return f'Magazyn w miescie {self.city} przy ulicy {self.street}.'


class KlientDetaliczny:
    def __init__(self, client_id, name: str, surname: str, street: str, city: str, country: str,
                 email: str, phone: str):
        self.client_id = client_id
        self.name = name
        self.surname = surname
        self.street = street
        self.city = city
        self.country = country
        self.email = email
        self.phone = phone

    def __str__(self):
        return f'Klient detaliczny {self.client_id} {self.name} {self.surname}, telefon kontaktowy {self.phone}'


class KlientBiznesowy:
    def __init__(self, client_id: str, name: str, surname: str, street: str, city: str, country: str, email: str,
                 phone: str, nip: str):
        self.client_id = client_id
        self.name = name
        self.surname = surname
        self.street = street
        self.city = city
        self.country = country
        self.email = email
        self.phone = phone
        self.nip = nip

    def __str__(self):
        return f'Klient biznesowy {self.client_id} {self.name} {self.surname}, telefon kontaktowy {self.phone}'


class Zamowienie:
    def __init__(self, order_id: str, product: Produkt, quantity: int, client_d: KlientDetaliczny,
                 client_b: KlientBiznesowy):
        self.order_id = order_id
        self.product = product
        self.quantity = quantity
        self.client_d = client_d
        self.client_b = client_b

    def __str__(self):
        return f'Zamowienie nr {self.order_id} na produkt {self.product.__str__()} w ilosci  {self.quantity} sztuk. ' \
           f'Zamawiajacy detaliczny: {self.client_d}, zamawiajacy biznesowy:  {self.client_b}. '


def order_value(product_price: float, quantity: int) -> float:
        order_value_calculation = product_price ** quantity
        return order_value_calculation


print(order_value(product_price, quantity))


def client_address(street: str, city: str, country: str) -> str:
    address_preparation = street + " " + city + " " + country
    return address_preparation


result = client_address(street, city, country)
print(result)


produkt1 = Produkt("podzespol1", "czarny", "Lenovo", "S670", 150)
produkt2 = Produkt("podzespol2", "bialy", "Asus", "F360", 230)
produkt3 = Produkt("podzespol3", "szary", "Lenovo", "BSWIN", 112)
magazyn1 = Magazyn("Orla 5", "Katowice", "Polska", "magazyn@gmail.com", "600 700 800")
klient_d1 = KlientDetaliczny("mkow001", "Marek" "Kowalski", "Rolna 12", "Katowice", "Poland", "mkowal@gmail.com",
                             "600 555 900")
klient_b1 = KlientBiznesowy("Jan", "Nowak", "Prosta 50", "Sosnowiec", "Poland", "jnow@gmail.com", "600 555 900",
                            "123456789")
zamowienie1 = Zamowienie("ZNov281", produkt1, 2, klient_d1, "brak")
zamowienie2 = Zamowienie("ZNov282", produkt2, 1, klient_d1, "brak")
zamowienie3 = Zamowienie("ZNov283", produkt3, 20, "", klient_b1)
