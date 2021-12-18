# ad1
# #for i in range(0, 10):
#   print('PyCharm')

# ad2
# import this

# ad3
# print("Hello Kasia")
# name = input()
# print("Hello " + name)
# print(f"Hello {name}, are you sure your name is {name}")

# ad4
# print(f"Next year you will be {int(input()) + 1}")

# ad5

# var_float = 42.0
# print(id(var_float))
# var_float = "ala ma kota"
# print(id(var_float))
# zmienna : str = 42.0

# ad6
# lista = list()
# print(lista)
# print(id(lista))
# print(type(lista))

# lista.append(300)

# lista = list()
# print(lista)
# print(id(lista))
# print(type(lista))

# ad7

# def print_object_info(what: list) -> bool:
#    print(what)
#    print(id(what))
#    print(type(what))
#    return True

# lista = list()
# print_object_info(lista)

# lista.append(300)
# print_object_info(lista)

# ad8
# stałe wyglądają jak zmienne, zapisujemy dużymi literami

# DAYS_IN_WEEK = 7

# sleep_per_day = list()
# sleep_per_day.append(6.2)
# sleep_per_day.append(7)
# sleep_per_day.append(8)
# sleep_per_day.append(5)
# sleep_per_day.append(6.5)
# sleep_per_day.append(7.1)
# sleep_per_day.append(8.5)

# print(f"There are {len(sleep_per_day)} sleeping nights")

# for idx, day in enumerate(sleep_per_day):
#   print(f"{idx} - {day}")
# 1 day sleep = 6.2

# sum_of_sleep = 0
# for day in sleep_per_day:
#     sum_of_sleep += day

# print(f"Average sleep time is: {(sum_of_sleep / len(sleep_per_day)):.2f}")

# Inne sposoby rozwiązania:
# 1. Znaleźć gotową bibliotekę, np. numpy/pandas
# 2. Lambda
# 3. Dict/List comprahension

# ad.9


def is_leap_year(year: int) -> bool:
    if not year % 400:
        return True
    if not year % 4 and year % 100:
        return True
    return False


print(is_leap_year(year=1600))
