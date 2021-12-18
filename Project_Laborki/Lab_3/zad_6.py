def podaj_dwie_listy(lista1: list, lista2: list) -> list:
    zlaczenie_list = list(set(lista1 + lista2))
    for x in range(len(zlaczenie_list)):
        zlaczenie_list[x] = zlaczenie_list[x] ** 3
    return zlaczenie_list


result = podaj_dwie_listy([1, 2, 3, 4], [3, 4, 5, 6])
print(result)

# lub


def merge_two_lists(first_list: list, second_list: list) -> list:
    merged_list = list(set(first_list + second_list))
    for count, value in enumerate(merged_list):
        # for x in range(len(merged_list)):
        merged_list[count] = merged_list[count] ** 3

    return merged_list


print("merge_two_lists result:")
print(merge_two_lists([1, 2, 3, 4], [4, 5]))
