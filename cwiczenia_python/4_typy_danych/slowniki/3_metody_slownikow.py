slownik_owocow = {
    "klucz": "wartosc",
    "Artur": "Ananas",
    "Basia": "Banan",
    "Celina": "Cytryna",
    "Dawid": "Daktyle",
    "Ewa": "Eszeweria"
}

# Metoda Zwracjące Klucze (Keys)
klucze = slownik_owocow.keys()  # zwraca typ danych dict_keys
print(f"klucze to: {klucze}")
print("typ kluczy:", type(klucze))
print()

lista_kluczy = list(klucze) # przekształca typ danych z dict_keys na list
print(f"lista_kluczy to: {lista_kluczy}")
print("typ lista kluczy:", type(lista_kluczy))
print()

# Metoda Zwracjące Wartości (Values)
wartosci = slownik_owocow.values()  # zwraca typ danych dict_values
print(f"wartości to: {wartosci}")
print("typ wartości:", type(wartosci))
print()

# Metoda Zwracjące Pary Klucz-Wartość (Items)
pary = slownik_owocow.items()  # zwraca typ danych dict_items
print(f"pary to: {pary}")
print("typ par:", type(pary))
print()

print("pojedyncza para:", list(pary)[1])

# funkcja do tworzenia dict() na analogini int() i list()
int("5")
list(  (1, 2, 3, 4)  )  # list przyjmuje 1 argument
liczby_1 = dict(a=1, b=1, c=1)
liczby_2 = {
    "a": 1,
    "b": 2,
    "c": 3
}
print(liczby_1)
print(liczby_2)

