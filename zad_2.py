print("a. Utwórz funkcję, która otrzyma w parametrze listę 5 imion, a następnie wyświetli każde z nich.")
print("")


def podaj_imiona(imiona: [str]):
    print(f"{imiona[0]}, {imiona[1]}, {imiona[2]}, {imiona[3]}, {imiona[4]}")


podaj_imiona(["Kasia", "Asia", "Basia", "Zosia", "Tosia"])

print("")
print("b. Utwórz funkcję, która otrzyma w parametrze listę zawierającą 5 dowolnych liczb, "
      "każdy jej element pomnoży przez 2, a na końcu ją zwróci.")
print("Zadanie należy wykonać w 2 wersjach:")
print("     i. Wykorzystując pętle for")
print("")


def podaj_liczby_v1(liczby_v1: [int]):
    for liczba_v1 in liczby_v1:
        print(liczba_v1 * 2)


podaj_liczby_v1([5, 6, 7, 8, 9])

print("")
print("     ii.Wykorzystując listę składaną")
print("")


def podaj_liczby_v2(liczby_v2: [int]):
    liczby_podwojone_v2 = [2*liczba_v2 for liczba_v2 in liczby_v2]
    print(liczby_podwojone_v2)


podaj_liczby_v2([10, 11, 12, 13, 14])


print("")
print("c. Utwórz pętlę iterującą po liście zawierającej 10 liczb (rekomendowane "
      "wykorzystanie funkcji range), która wyświetla jedynie parzyste elementy.")
print("")


for i in range(10):
    if i % 2:
        continue
    print(i)

print("")
print("d. Utwórz pętlę iterującą po liście zawierającej 10 liczb (rekomendowane "
      "wykorzystanie funkcji range ), która wyświetla co drugi element.")
print("")


for i in range(10):
    if i % 2:
        print(i)
        continue
