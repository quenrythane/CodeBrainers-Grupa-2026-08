"""
lista_imion = ["Adam", "Basia", "Cezary", "Damian", "Ewa"]
Używając pętli FOR, napisz cześć do każdej osoby z listy, pisząc ich imię kapslokiem (.upper()).
"""

lista_imion = ["Adam", "Basia", "Cezary", "Damian", "Ewa"]

for imie in lista_imion:
    print("Start obiegu pętli dla imienia", imie)
    print("Czesc", imie.upper())
    print("Koniec obiegu pętli dla imienia", imie, "\n")

print("Koniec programu")