lista_imion = ["Adam", "Basia", "Cezary", "Damian", "Ewa"]

for imie in lista_imion:
    if imie.endswith("a"):
        imie = imie.upper()
    elif imie == "Cezary":
        imie *= 3
    else:
        imie = imie.lower()
    print("Czesc", imie)





