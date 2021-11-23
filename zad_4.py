def podaj_trzy_liczby(liczba1: int, liczba2: int, liczba3: int) -> bool:
    czy_suma_dwoch_pierwszych_wieksza_od_trzeciej = liczba1 + liczba2 >= liczba3
    return czy_suma_dwoch_pierwszych_wieksza_od_trzeciej


result = podaj_trzy_liczby(1, 2, 5)
print(result)
