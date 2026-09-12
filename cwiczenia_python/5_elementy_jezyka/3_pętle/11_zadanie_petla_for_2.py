slownik_owocow = {
    "klucz": "wartosc",
    "Artur": "Ananas",
    "Basia": "Banan",
    "Celina": "Cytryna",
    "Dawid": "Daktyle",
    "Ewa": "Eszeweria"
}


"""
z podanego słownika wyprintuj wszystkie żeńskie imiona
klucze = slownik_owocow.keys()
"""
# for i in slownik_owocow:
#     print(i)


# lista_imiona = list(slownik_owocow.keys())  # opcjonalne
for imie in slownik_owocow.keys():
    if imie.endswith("a"):
        print(imie)

"""
z podanego słownika wyprintuj wszystkie owoce której mają więcej niż 6 liter
klucze = slownik_owocow.keys()
"""

for owoc in list(slownik_owocow.values())[1:]:  # sliceujemy, żeby pozbyć się pierwszej niepoprawnej wartości
    if len(owoc) > 6:
        print(owoc)
