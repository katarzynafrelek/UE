def podaj_liczbe_parzysta(liczba: int) -> bool:
    reszta = liczba % 2
    if reszta == 0:
        return True
    else:
        return False


czy_parzysta = podaj_liczbe_parzysta(5)
if czy_parzysta:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")
