from Kolokwium2.Klasy_kolokwium.Developer import Developer
from Kolokwium2.Klasy_kolokwium.Mieszkanie import Mieszkanie
from Kolokwium2.Klasy_kolokwium.Dom import Dom
from Kolokwium2.Klasy_kolokwium.Zamowienie import Zamowienie

Developer1 = Developer("DomBud", "ul. Piekarska 3 Katowice", "123456789", "111122223333")
Mieszkanie1 = Mieszkanie("ul. Daleka 5 Katowice", "4", 70.5, "3", 899999.00)
Mieszkanie2 = Mieszkanie("ul. Bliska 5 Chorzow", "3", 35, "8", 490999.99)
Dom1 = Dom("ul. Wiejska 12 Rybnik", "5", 125.8, 1800999.99)
Dom2 = Dom("ul. Miejska 9 Bytom", "6", 230, 2350199.59)
Zamowienie1 = Zamowienie("ZAM1", Developer1, "Jan Kowalski", None, Dom1, 2)

print(Zamowienie1.__str__())
print(Zamowienie1.order_value_calculation())
print(Zamowienie1.ordered_surface())
