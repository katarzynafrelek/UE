# Zadanie 1


def podaj_imie_nazwisko(name: str, surname: str) -> str:
    powitanie = str("Cześć " + name + " " + surname + "!")
    return powitanie


result = podaj_imie_nazwisko("Katarzyna", "Frelek")
print(result)

# Zadanie 2


def podaj_dwie_liczby(liczba1: int, liczba2: int) -> int:
    wynik_mnozenia = liczba1 * liczba2
    return wynik_mnozenia


result = podaj_dwie_liczby(3, 4)
print(result)

# Zadanie 3


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

# Zadanie 4


def podaj_trzy_liczby(liczba1: int, liczba2: int, liczba3: int) -> bool:
    czy_suma_dwoch_pierwszych_wieksza_od_trzeciej = liczba1 + liczba2 >= liczba3
    return czy_suma_dwoch_pierwszych_wieksza_od_trzeciej


result = podaj_trzy_liczby(1, 2, 5)
print(result)

# Zadanie 5


def podaj_dwa_argumenty(lista: list, liczba: int) -> bool:
    czy_liczba_w_liscie = liczba in lista
    return czy_liczba_w_liscie


result = podaj_dwa_argumenty([13, 45, 742], 13)
print(result)

# Zadanie 6


def podaj_dwie_listy(lista1: list, lista2: list) -> list:
    zlaczenie_list = list(set(lista1 + lista2))
    for x in range(len(zlaczenie_list)):
        zlaczenie_list[x] = zlaczenie_list[x] ** 3
    return zlaczenie_list


result = podaj_dwie_listy([1, 2, 3, 4], [3, 4, 5, 6])
print(result)

