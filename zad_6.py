def podaj_dwie_listy(lista1: list, lista2: list) -> list:
    zlaczenie_list = list(set(lista1 + lista2))
    for x in range(len(zlaczenie_list)):
        zlaczenie_list[x] = zlaczenie_list[x] ** 3
    return zlaczenie_list


result = podaj_dwie_listy([1, 2, 3, 4], [3, 4, 5, 6])
print(result)
