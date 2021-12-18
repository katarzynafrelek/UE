def podaj_imie_nazwisko(name: str, surname: str) -> str:
    powitanie = str("Cześć " + name + " " + surname + "!")
    return powitanie


result = podaj_imie_nazwisko("Katarzyna", "Frelek")
print(result)
