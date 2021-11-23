def podaj_dwa_argumenty(lista: list, liczba: int) -> bool:
    czy_liczba_w_liscie = liczba in lista
    return czy_liczba_w_liscie


result = podaj_dwa_argumenty([13, 45, 742], 13)
print(result)
