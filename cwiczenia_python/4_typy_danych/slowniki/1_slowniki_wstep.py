# CIEKAWOSTKA: elementy złożonych typów mogą być dowolną strukturą danych, oprócz samych siebie
lista = [1, "a", 2.5, True, [1, 2, 3], print, print()]
print(lista)


lista_imiona = ["Artur", "Basia", "Celina", "Dawid", "Ewa"]


artur = [0]

slownik_imion = {
    # 1: "Artur",
    2: "Basia",
    3: "Celina",
    4: "Dawid",
    5: "Ewa",
    "xd": "nowy wpis xd",
    1: "Kolejny Maciek"
}


a = slownik_imion[1]
print(a)
